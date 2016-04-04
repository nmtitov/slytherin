# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('file', models.ImageField(blank=True, upload_to='images', null=True)),
                ('caption', models.CharField(blank=True, max_length=1024, null=True))
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('published', models.BooleanField(default=False, db_index=True)),
                ('publication_date', models.DateTimeField(blank=True, null=True)),
                ('slug', models.CharField(db_index=True, max_length=1024, unique=True)),
                ('title', models.CharField(max_length=1024)),
                ('lead', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('thumbnail_image', models.OneToOneField(to='blog.Image', related_name='thumbnail_image', blank=True, null=True)),
                ('title_before', models.CharField(blank=True, max_length=1024)),
                ('title_after', models.CharField(blank=True, max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('blog_title', models.CharField(max_length=1024)),
                ('blog_copyright', models.CharField(max_length=1024)),
                ('author_email', models.EmailField(max_length=254)),
                ('counter_yandex_metrika', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'settings',
            },
            bases=(models.Model,),
        ),
    ]
