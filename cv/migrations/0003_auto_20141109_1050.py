# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20141023_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_title',
            field=models.CharField(max_length=1024, default='Untitled'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
    ]
