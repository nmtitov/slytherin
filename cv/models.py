from django.db import models
from django.template.defaultfilters import slugify
import os


def get_image_path(screenshot, filename):
    return os.path.join("screenshots", slugify(screenshot.project.title), filename)


class Project(models.Model):
    title = models.CharField(max_length=1024)
    lead = models.TextField(blank=True)
    body = models.TextField(blank=True)
    download_url = models.CharField(max_length=1024, blank=True)
    store_button = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def __repr__(self):
        return self.__unicode__()

    def slug(self):
        return slugify(self.title)


class Screenshot(models.Model):
    project = models.ForeignKey(Project)
    image_path = models.ImageField(upload_to=get_image_path, blank=True, null=True)


