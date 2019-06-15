from django.db import models
from uuslug import slugify


class Section(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, db_index=True, unique=True, editable=False)
    verbose_title = models.CharField(max_length=1024)
    priority = models.SmallIntegerField(default=0)

    @property
    def display_title(self):
        return self.verbose_title if self.verbose_title else self.title

    @classmethod
    def get_home(cls):
        return cls.objects.order_by('-priority').first()

    @classmethod
    def get_by_slug(cls, slug):
        return cls.objects.get(slug=slug)

    @classmethod
    def list(cls):
        return list(cls.objects.all().order_by('-priority'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, max_length=128, word_boundary=True, save_order=True)
        super().save(*args, **kwargs)

    def section_html_id(self):
        return "page_{}".format(self.slug)

    def __str__(self):
        return self.title
