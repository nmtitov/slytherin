# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 10:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170306_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='verbose_title',
        ),
        migrations.RemoveField(
            model_name='section',
            name='verbose_title',
        ),
    ]
