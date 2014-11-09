# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0015_post_screencast'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=redactor.fields.RedactorField(blank=True, null=True, verbose_name='Body'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='lead',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(unique=True, default=1, db_index=True, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screencast',
            name='body',
            field=redactor.fields.RedactorField(blank=True, null=True, verbose_name='Body'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='screencast',
            name='lead',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='screencast',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='screencast',
            name='published',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='screencast',
            name='slug',
            field=models.CharField(unique=True, default=1, db_index=True, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='screencast',
            name='title',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=redactor.fields.RedactorField(blank=True, null=True, verbose_name='Body'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='lead',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
            preserve_default=True,
        ),
    ]
