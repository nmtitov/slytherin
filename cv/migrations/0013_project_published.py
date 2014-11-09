# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0012_project_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='published',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]
