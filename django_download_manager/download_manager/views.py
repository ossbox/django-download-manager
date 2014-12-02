# -*- coding: utf-8 -*-
# Copyright (c) 2014 - Luís A. Bastião Silva

# Author: Luís A. Bastião Silva

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from django.shortcuts import render

from django.views.generic import View
from django.views.generic.base import TemplateView

from django.views.generic.detail import SingleObjectMixin

from download_manager.models import *
from django.views import generic

from django.http import HttpResponse
import uuid

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.static import serve

import os

class ThanksView(TemplateView):

    template_name = "thanks.html"



    def get(self, request,*args, **kwargs):
        self.object = ""
        return super(ThanksView, self).get(request, *args, **kwargs)



class AcceptView(SingleObjectMixin, TemplateView):

    template_name = "accept.html"


    def get(self, request, hash_id=None,*args, **kwargs):
        self.object = ""

        print hash_id
        dr = DownloadRequest.objects.get(hashLink=hash_id)
        if (not dr.pending):
            html = "<html><body>This request has been already handled. Approved = %s </body></html>" % str(dr.approved)
            return HttpResponse(html)
        dr.pending = False
        dr.approved = True
        dr.save()
        # This could be refactor (next time I hack )
        subject, from_email, to = settings.PROJECT_NAME + ' - Download Manager', settings.DEFAULT_FROM_EMAIL, dr.communityUser.email

        html_content = '<p>Dear %s,</p>' % dr.communityUser.name
        html_content += 'Please download: %s <br />' % (settings.BASE_URL + "dw/link/" + hash_id)

        html_content += "<br /><br />See you next download! "
        html_content += "<br />Dicoogle Team. "


        msg = EmailMultiAlternatives(subject, "", from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


        return super(AcceptView, self).get(request, *args, **kwargs)

class RejectView(SingleObjectMixin, TemplateView):

    template_name = "reject.html"
    def get(self, request,  hash_id=None,*args, **kwargs):
        self.object = ""
        print "reject"
        print hash_id
        dr = DownloadRequest.objects.get(hashLink=hash_id)
        if (not dr.pending):
            html = "<html><body>This request has been already handled. Approved = %s </body></html>" % str(dr.approved)
            return HttpResponse(html)

        dr.pending = False
        dr.save()

                # This could be refactor (next time I hack )
        subject, from_email, to = settings.PROJECT_NAME + ' - Download Manager', settings.DEFAULT_FROM_EMAIL, dr.communityUser.email

        html_content = '<p>Dear %s,</p>' % dr.communityUser.name
        html_content += 'Your download request has been rejected. <br />'

        html_content += "<br /><br />Best Regards, "
        html_content += "<br />Dicoogle Team. "


        msg = EmailMultiAlternatives(subject, "", from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return super(RejectView, self).get(request, *args, **kwargs)

class HomePageView(SingleObjectMixin, TemplateView):

    template_name = "form.html"

    def get(self, request, *args, **kwargs):
        self.object = ""
        return super(HomePageView, self).get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        self.object = ""
        if request.method == 'POST':
            email = request.POST.get("email", "")

            try:
                _user = CommunityUser.objects.get(email=email)
            except (CommunityUser.DoesNotExist):
                _user = CommunityUser()

            _user.email = email
            _user.name = request.POST.get("name", "")
            _user.address = request.POST.get("address", "")
            _user.phone = request.POST.get("phone", "")
            _user.homepage = request.POST.get("homepage", "")
            _user.organization = request.POST.get("organization", "")
            _user.country = request.POST.get("country", "")
            _user.description = request.POST.get("description", "")
            _user.name = request.POST.get("name", "")
            _user.save()

            resource = request.GET.get('resource', 'http://www.dicoogle.com')
            _dr = DownloadRequest()
            _dr.communityUser=_user
            _dr.resource = resource
            _dr.hashLink =uuid.uuid4()
            _dr.save()

            direct = request.GET.get('direct', 'False')
            # This is a hard hack - I will fix it later.
            print direct
            if direct=="1":

                if (not _dr.resource.startswith('D_')):
                    return HttpResponse(status=400)

                hash_id = str(_dr.hashLink)
                dr = DownloadRequest.objects.get(hashLink=hash_id)
                dr.pending = False
                dr.approved = True
                dr.save()
                # This could be refactor (next time I hack )
                subject, from_email, to = settings.PROJECT_NAME + ' - Download Manager', settings.DEFAULT_FROM_EMAIL, dr.communityUser.email

                html_content = '<p>Dear %s,</p>' % dr.communityUser.name
                html_content += 'Please download: %s <br />' % (settings.BASE_URL + "dw/link/" + hash_id)

                html_content += "<br /><br />See you next download! "


                msg = EmailMultiAlternatives(subject, "", from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                return HttpResponseRedirect(reverse('thanks', ))




            print "sending email"
            print settings.ADMINS
            for (_n, _e) in settings.ADMINS:


                # This could be refactor (next time I hack )
                subject, from_email, to = settings.PROJECT_NAME + ' [DownloadRequest]', settings.DEFAULT_FROM_EMAIL, _e

                html_content = '<p>Dear Administrator,</p>'
                html_content += 'Please validate this download request:<br />'
                html_content += 'Name: : %s <br />' % _user.name
                html_content += 'Address:  %s <br />' % _user.address
                html_content += 'Email:  %s <br />' % _user.email
                html_content += 'Phone number:  %s <br />' % _user.phone
                html_content += 'Home Page/LinkedIn/or any other public profile available: %s <br />' % _user.homepage
                html_content += 'Company/Organization: :  %s <br />' % _user.organization
                html_content += 'Country: : %s <br />' % _user.country
                html_content += 'Dicoogle Interest (R&D, Comercial Use, Developer, Educational - please describe):  %s <br />' % _user.description
                html_content += 'Resource to download: : %s <br />' % _dr.resource

                html_content += "<br /> To accept: %s " % (settings.BASE_URL + "dw/accept/" + str(_dr.hashLink))
                html_content += "<br /> To reject: %s " % (settings.BASE_URL + "dw/reject/" + str(_dr.hashLink))


                html_content += "<br /><br />See you next download! "


                msg = EmailMultiAlternatives(subject, "", from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            #return super(HomePageView, self).get(request, *args, **kwargs)
            return HttpResponseRedirect(reverse('thanks', ))
        else:
            return HttpResponse(status=400)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['name'] = "Form"
        return context



class DownloadView(SingleObjectMixin, TemplateView):

    template_name = "form.html"

    def get(self, request, hash_id=None, *args, **kwargs):
        self.object = ""

        dr = DownloadRequest.objects.get(hashLink=hash_id)
        if not dr.approved:
            return HttpResponse(status=400)



        filepath = settings.DOWNLOAD_FOLDER + dr.resource

        mimetype = "application/octet-stream"
        f = open(filepath, 'r')
        response = HttpResponse(f.read(), content_type=mimetype)
        response["Content-Disposition"]= "attachment; filename=%s" % dr.resource

        return response

        #return super(DownloadView, self).get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        self.object = ""
        print "check what is happening"
        return super(DownloadView, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(DownloadView, self).get_context_data(**kwargs)
        context['name'] = "Form"
        return context
