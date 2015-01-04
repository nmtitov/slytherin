# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0016_auto_20141109_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail_url',
            field=models.CharField(default='https://img-fotki.yandex.ru/get/15523/89716622.0/0_11b4af_c2808b72_orig',
                                   max_length=1024),
            preserve_default=False,
        ),
    ]
