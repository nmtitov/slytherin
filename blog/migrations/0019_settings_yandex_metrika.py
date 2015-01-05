# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='yandex_metrika',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
