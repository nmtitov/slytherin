# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20141109_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='process_title',
            field=models.CharField(max_length=1024),
            preserve_default=True,
        ),
    ]
