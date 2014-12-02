# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_manager', '0002_auto_20141202_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityuser',
            name='country',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
