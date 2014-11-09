from django.db import models
from django.template.defaultfilters import slugify
import os
from redactor.fields import RedactorField



def get_image_path(screenshot, filename):
    return os.path.join("screenshots", slugify(screenshot.project.title), filename)


class Project(models.Model):
    project_title = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    lead = models.TextField(blank=True)
    body = models.TextField(blank=True)
    download_url = models.CharField(max_length=1024, blank=True)
    store_button = models.TextField(blank=True)
    pub_date = models.DateTimeField('date published')
    content = RedactorField(verbose_name=u'Content')

    def __str__(self):
        return self.project_title

    def slug(self):
        return slugify(self.title)

    def preview_url(self):
        try:
            return self.screenshot_set.all()[0].image_path.url
        except IndexError:
            return None


class Screenshot(models.Model):
    project = models.ForeignKey(Project)
    image_path = models.ImageField(upload_to=get_image_path, blank=True, null=True)


