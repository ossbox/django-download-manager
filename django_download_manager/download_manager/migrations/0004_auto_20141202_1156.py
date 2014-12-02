# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('download_manager', '0003_communityuser_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityuser',
            name='removed',
            field=models.BooleanField(default=False, help_text=b''),
            preserve_default=True,
        ),
    ]
