# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20141109_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='preview',
            field=models.OneToOneField(null=True, to='blog.Screenshot', related_name='preview'),
            preserve_default=True,
        ),
    ]
