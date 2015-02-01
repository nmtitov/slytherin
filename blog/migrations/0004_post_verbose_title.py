# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_side'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='verbose_title',
            field=models.CharField(max_length=1024, default=''),
            preserve_default=False,
        ),
    ]
