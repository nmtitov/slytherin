from django.db import models
from django.template.defaultfilters import slugify
import os
from redactor.fields import RedactorField


def get_image_path(screenshot, filename):
    return os.path.join("screenshots", slugify(screenshot.project.title), filename)


class Post(models.Model):
    published = models.BooleanField(default=False, db_index=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    title = models.CharField(max_length=1024)
    slug = models.CharField(max_length=1024, db_index=True, null=False, unique=True)
    lead = models.TextField(blank=True, null=True)
    body = RedactorField(verbose_name="Body", blank=True, null=True)
    preview = models.OneToOneField('Screenshot', related_name='preview', blank=True, null=True, unique=False)
    project_title = models.CharField(max_length=1024)
    download_url = models.CharField(max_length=1024, blank=True)
    store_button = models.TextField(blank=True)
    process_title = models.CharField(max_length=1024)
    process_description = RedactorField(verbose_name="Process description")
    thumbnail_url = models.CharField(max_length=1024)

    def preview_url(self):
        try:
            return self.screenshot_set.all()[0].image_path.url
        except IndexError:
            return None

    def auto_slug(self):
        return slugify(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                self.slug = self.auto_slug()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Screenshot(models.Model):
    project = models.ForeignKey(Post)
    image_path = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.image_path.url


class Settings(models.Model):
    title = models.CharField(max_length=1024)
    copyright = models.CharField(max_length=1024)
    email = models.EmailField(max_length=254)
    yandex_metrika = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "settings"
