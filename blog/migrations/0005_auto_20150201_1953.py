# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_verbose_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='alt',
            field=models.CharField(null=True, blank=True, max_length=1024),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='retina',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.CharField(null=True, blank=True, max_length=32),
            preserve_default=True,
        ),
        migrations.AlterIndexTogether(
            name='image',
            index_together=set([('post', 'slug')]),
        ),
    ]
