# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 12:45
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_post_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='side',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
