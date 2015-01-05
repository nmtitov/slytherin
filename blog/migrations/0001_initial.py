# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('published', models.BooleanField(default=False, db_index=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('title', models.CharField(max_length=1024)),
                ('slug', models.CharField(unique=True, db_index=True, max_length=1024)),
                ('lead', models.TextField(blank=True, null=True)),
                ('body', redactor.fields.RedactorField(blank=True, null=True, verbose_name='Body')),
                ('project_title', models.CharField(max_length=1024)),
                ('download_url', models.CharField(blank=True, max_length=1024)),
                ('store_button', models.TextField(blank=True)),
                ('process_title', models.CharField(max_length=1024)),
                ('process_description', redactor.fields.RedactorField(verbose_name='Process description')),
                ('thumbnail_url', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image_path', models.ImageField(blank=True, null=True, upload_to=blog.models.get_image_path)),
                ('project', models.ForeignKey(to='blog.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=1024)),
                ('copyright', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=254)),
                ('yandex_metrika', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'settings',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.OneToOneField(related_name='preview', to='blog.Screenshot', blank=True, null=True),
            preserve_default=True,
        ),
    ]
