# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0013_project_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='preview',
            field=models.OneToOneField(related_name='preview', blank=True, to='cv.Screenshot', null=True),
            preserve_default=True,
        ),
    ]
