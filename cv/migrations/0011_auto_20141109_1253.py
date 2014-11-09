# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_auto_20141109_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=redactor.fields.RedactorField(verbose_name='Body'),
            preserve_default=True,
        ),
    ]
