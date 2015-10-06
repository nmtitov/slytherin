# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20151006_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_after',
            field=models.CharField(blank=True, max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_before',
            field=models.CharField(blank=True, max_length=1024),
            preserve_default=True,
        ),
    ]
