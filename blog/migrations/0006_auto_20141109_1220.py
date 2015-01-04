# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.template.defaultfilters import slugify


def add_slug_to_projects(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Project = apps.get_model("blog", "Project")
    for p in Project.objects.all():
        p.slug = slugify(p.title)
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_project_slug'),
    ]

    operations = [
        migrations.RunPython(add_slug_to_projects),
    ]
