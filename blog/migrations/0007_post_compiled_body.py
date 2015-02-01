# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150201_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='compiled_body',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
