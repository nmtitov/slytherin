# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20141109_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=redactor.fields.RedactorField(default='No content yet', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
