# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_image_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_after',
            field=models.CharField(blank=True, default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_before',
            field=models.CharField(blank=True, default='', max_length=1024),
            preserve_default=False,
        ),
    ]
