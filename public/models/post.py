from collections import defaultdict
from django.db import models
from uuslug import slugify
from .secton import Section


class Post(models.Model):
    section = models.ForeignKey(Section, related_name='posts', db_index=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=256)
    internal_title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)
    thumbnail = models.TextField(blank=True)
    body = models.TextField(blank=True)
    sidebar = models.TextField(blank=True)
    hidden = models.BooleanField(default=False, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)
    release_date = models.DateTimeField(blank=True, null=True)

    @classmethod
    def list_by_section(cls, section):
        return list(cls.objects.filter(section=section, hidden=False).order_by('-release_date', '-created_date'))

    @classmethod
    def list_by_section_group_by_year(cls, section):
        # Get model objects
        posts = Post.list_by_section(section=section)

        # Group posts by year
        default_dict = defaultdict(list)
        for post in posts:
            key = post.release_date.year if post.release_date else None
            default_dict[key].append(post)

        return dict(default_dict)

    @classmethod
    def get_by_section_and_slug(cls, section, slug: str):
        return Post.objects.get(section=section, slug=slug, hidden=False)

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = slugify(self.title, max_length=128, word_boundary=True, save_order=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
