# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('address', models.CharField(unique=True, max_length=255)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('phone', models.CharField(unique=True, max_length=255)),
                ('homepage', models.CharField(unique=True, max_length=255)),
                ('facebook', models.CharField(unique=True, max_length=255)),
                ('linkedin', models.CharField(unique=True, max_length=255)),
                ('company', models.CharField(unique=True, max_length=255)),
                ('organization', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('last_modification', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('removed', models.BooleanField(default=False, help_text=b'Remove logically the fingerprint')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DownloadRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resource', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(600)])),
                ('hashLink', models.CharField(unique=True, max_length=255)),
                ('last_modification', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('pending', models.BooleanField(default=True, help_text=b'Pending?')),
                ('approved', models.BooleanField(default=False, help_text=b'Approved?')),
                ('communityUser', models.ForeignKey(to='download_manager.CommunityUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
