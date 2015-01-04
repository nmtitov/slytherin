# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screenshot',
            old_name='profile_image',
            new_name='image_path',
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='download_url',
            field=models.CharField(max_length=1024, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='lead',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='store_button',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
