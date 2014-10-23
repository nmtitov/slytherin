# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cv.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('lead', models.TextField()),
                ('body', models.TextField()),
                ('download_url', models.CharField(max_length=1024)),
                ('store_button', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_image', models.ImageField(null=True, upload_to=cv.models.get_image_path, blank=True)),
                ('project', models.ForeignKey(to='cv.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
