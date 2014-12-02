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
            _user.description = request.POST.get("description", "")
            _user.name = request.POST.get("name", "")
            _user.save()

            resource = request.GET.get('resource', 'http://www.dicoogle.com')

            _dr = DownloadRequest()
            _dr.communityUser=_user
            _dr.resource = resource
            _dr.hashLink =uuid.uuid4()
            _dr.save()


            return super(HomePageView, self).get(request, *args, **kwargs)
        else:
            return HttpResponse(status=400)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['name'] = "Form"
        return context



class DownloadView(SingleObjectMixin, TemplateView):

    template_name = "form.html"

    def get(self, request, *args, **kwargs):
        self.object = ""
        return super(DownloadView, self).get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        self.object = ""
        print "check what is happening"
        return super(DownloadView, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(DownloadView, self).get_context_data(**kwargs)
        context['name'] = "Form"
        return context
