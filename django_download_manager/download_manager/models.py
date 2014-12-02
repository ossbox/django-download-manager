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


from django.db import models

from django.core.validators import *

class CommunityUser(models.Model):

    name =  models.CharField(max_length=255, unique=False, blank=False, null=False)
    address =  models.CharField(max_length=255, unique=False, blank=False, null=False)
    email =  models.CharField(max_length=255, unique=True, blank=False, null=False)
    phone =  models.CharField(max_length=255, unique=False, blank=False, null=False)
    homepage =  models.CharField(max_length=255, unique=False, blank=False, null=False)
    facebook =  models.CharField(max_length=255, unique=False, blank=False, null=False)
    linkedin =  models.CharField(max_length=255, unique=False, blank=False, null=False)
    company =  models.CharField(max_length=255, unique=False, blank=False, null=False)
    organization =  models.CharField(max_length=255, unique=False, blank=False, null=False)

    description = models.TextField(blank=True, null=True)

    last_modification = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    removed = models.BooleanField(default=False, help_text="Remove logically the fingerprint")

    def __unicode__(self):
        return " Name " + self.name

class DownloadRequest(models.Model):
    communityUser =  models.ForeignKey(CommunityUser, null=False)
    resource = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(600)])
    hashLink =  models.CharField(max_length=255, unique=True, blank=False, null=False)
    last_modification = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    pending = models.BooleanField(default=True, help_text="Pending?")
    approved = models.BooleanField(default=False, help_text="Approved?")


    def __unicode__(self):
        return str(self.communityUser) + " to " + self.resource
