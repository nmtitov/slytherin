# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0007_auto_20141109_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='content',
        ),
        migrations.AddField(
            model_name='project',
            name='process',
            field=redactor.fields.RedactorField(default='No process description yet', verbose_name='Process'),
            preserve_default=False,
        ),
    ]
