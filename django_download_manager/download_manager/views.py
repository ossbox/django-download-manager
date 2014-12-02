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


class HomePageView(SingleObjectMixin, TemplateView):

    template_name = "form.html"

    def get(self, request, *args, **kwargs):
        self.object = ""
        return super(HomePageView, self).get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        self.object = ""
        print "check what is happening"
        return super(HomePageView, self).get(request, *args, **kwargs)


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
