# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150201_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='compiled_body',
            field=models.TextField(blank=True, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('post', 'slug')]),
        ),
    ]
