from django.db import models
from uuslug import slugify
from .secton import Section


class Post(models.Model):
    section = models.ForeignKey(Section, related_name='posts', db_index=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)
    thumbnail = models.TextField()
    body = models.TextField()
    side = models.TextField()
    hidden = models.BooleanField(default=False, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    release_date = models.DateTimeField(blank=True, null=True)

    @classmethod
    def list_by_section(cls, section):
        return list(cls.objects.filter(section=section, hidden=False).order_by('-created_date'))

    @classmethod
    def get_by_section_and_slug(cls, section, slug: str):
        return Post.objects.get(section=section, slug=slug, hidden=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, max_length=128, word_boundary=True, save_order=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
