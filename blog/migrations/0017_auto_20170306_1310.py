# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-06 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_post_side'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='draft',
            new_name='hidden',
        ),
    ]
