# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20141109_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='process',
        ),
        migrations.AddField(
            model_name='project',
            name='process_description',
            field=redactor.fields.RedactorField(default='No process description yet', verbose_name='Process description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='process_title',
            field=redactor.fields.RedactorField(default='No process title yet', verbose_name='Process title'),
            preserve_default=False,
        ),
    ]
