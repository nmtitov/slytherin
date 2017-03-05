# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


# def create_default_section(apps, schema_editor):
#     section_model = apps.get_model("blog", "Section")
#     section_model.objects.create()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('file', models.ImageField(upload_to='images')),
                ('caption', models.CharField(blank=True, max_length=1024, null=True)),
                ('alt', models.CharField(null=True, blank=True, max_length=1024)),
                ('retina', models.BooleanField(default=False)),
                ('slug', models.CharField(null=True, blank=True, max_length=32)),
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
                ('title_before', models.CharField(blank=True, max_length=1024)),
                ('title', models.CharField(max_length=1024)),
                ('title_after', models.CharField(blank=True, max_length=1024)),
                ('verbose_title', models.CharField(max_length=1024)),
                ('lead', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('compiled_body', models.TextField(blank=True, null=True, editable=False)),
                ('release_date', models.DateTimeField(blank=True, null=True)),
                ('thumbnail_image', models.OneToOneField(to='blog.Image', related_name='thumbnail_image', blank=True, null=True)),
                ('side', models.TextField(null=True, blank=True)),
                ('preview', models.BooleanField(default=False, db_index=True)),
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
        migrations.AlterIndexTogether(
            name='image',
            index_together=set([('post', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set([('post', 'slug')]),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('verbose_title', models.CharField(max_length=1024)),
                ('slug', models.CharField(max_length=32, unique=True)),
            ],
        ),
        # migrations.RunPython(create_default_section),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(on_delete=models.deletion.PROTECT, related_name='posts', to='blog.Section'),
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
