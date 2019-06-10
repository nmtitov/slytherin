# Generated by Django 2.2.2 on 2019-06-10 19:31

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=128, unique=True)),
                ('priority', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=1024)),
                ('blog_copyright', models.CharField(max_length=1024)),
                ('author_email', models.EmailField(max_length=254)),
                ('counter_yandex_metrika', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'settings',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(editable=False, max_length=256, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('hidden', models.BooleanField(db_index=True, default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='public.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images')),
                ('retina', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False, max_length=1024, unique=True)),
                ('alt', models.CharField(blank=True, editable=False, max_length=1024, null=True)),
                ('caption', models.CharField(blank=True, max_length=1024, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.Post')),
            ],
            options={
                'unique_together': {('post', 'slug')},
                'index_together': {('post', 'slug')},
            },
        ),
    ]
