# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_project_thumbnail_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('copyright', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'settings',
            },
            bases=(models.Model,),
        ),
    ]
