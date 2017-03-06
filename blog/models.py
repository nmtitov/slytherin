from django.db import models
from os import path as op
from bs4 import BeautifulSoup as Soup
from django.core.exceptions import ObjectDoesNotExist
from django.template import Template, Context
from typing import List, Type, TypeVar
from uuslug import slugify
from ckeditor.fields import RichTextField


S = TypeVar('S', bound='Section')
class Section(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, db_index=True, unique=True, editable=False)

    @classmethod
    def get_root(cls: Type['S']) -> S:
        return cls.objects.first()

    @classmethod
    def get_by_slug(cls: Type['S'], slug: str) -> S:
        return cls.objects.get(slug=slug)

    @classmethod
    def list(cls: Type['S']) -> List[S]:
        return list(cls.objects.all())

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, max_length=128, word_boundary=True, save_order=True)
        super().save(*args, **kwargs)

    def section_html_id(self):
        return "page_{}".format(self.slug)

    def __str__(self):
        return self.title


P = TypeVar('P', bound='Post')
class Post(models.Model):
    section = models.ForeignKey(Section, related_name='posts', db_index=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, db_index=True, unique=True, editable=False)
    thumbnail_image = models.OneToOneField('Image', related_name='thumbnail_image', blank=True, null=True, unique=False)
    body = RichTextField()
    # side = RichTextField(blank=True, null=True)
    draft = models.BooleanField(default=False, db_index=True)
    publication_date = models.DateTimeField(blank=True, null=True)

    @classmethod
    def list_by_section(cls: Type['P'], section: S) -> List[P]:
        return list(cls.objects.filter(section=section, draft=False).order_by('-publication_date'))

    @classmethod
    def get_by_section_and_slug(cls: Type['P'], section: S, slug: str) -> P:
        return Post.objects.get(section=section, slug=slug, draft=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, max_length=128, word_boundary=True, save_order=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post)
    file = models.ImageField(upload_to="images")
    retina = models.BooleanField(default=False)
    slug = models.SlugField(max_length=1024, db_index=True, unique=True, editable=False)
    alt = models.CharField(max_length=1024, blank=True, null=True, editable=False)
    caption = models.CharField(max_length=1024, blank=True, null=True)

    @property
    def height(self):
        return self.file.height // 2 if self.retina else self.file.height

    @property
    def width(self):
        return self.file.width // 2 if self.retina else self.file.width

    @property
    def size(self):
        return self.width, self.height

    @property
    def url(self):
        return self.file.url

    @property
    def figure_html(self):
        template = \
        """
        <figure class="post">
            <div class="container">
                <img src="{{ image.url }}"
                    {% if image.alt %} alt="{{ image.alt }}" {% endif %}
                    {% if image.caption %} title="{{ image.caption }}" {% endif %}
                    width="{{ image.width }}"
                    height="{{ image.height }}" />
            </div>
            {% if image.caption %}
            <figcaption>{{ image.caption }}</figcaption>
            {% endif %}
        </figure>
        """
        return Template(template).render(Context({'image': self}))

    def save(self, *args, **kwargs):
        if not self.id:
            name, ext = op.splitext(op.basename(self.file.name))
            self.slug = slugify(name, max_length=1024, word_boundary=True, save_order=True)
            self.alt = self.caption
        super().save(*args, **kwargs)

    def __str__(self):
        return "{post}-{image}".format(post=self.post.slug, image=self.slug)

    class Meta:
        index_together = unique_together = ["post", "slug"]


St = TypeVar('St', bound='Settings')
class Settings(models.Model):
    blog_title = models.CharField(max_length=1024)
    blog_copyright = models.CharField(max_length=1024)
    author_email = models.EmailField(max_length=254)
    counter_yandex_metrika = models.TextField(blank=True, null=True)

    @classmethod
    def get(cls: Type['St']) -> St:
        return cls.objects.first()

    def __str__(self):
        return self.blog_title


    class Meta:
        verbose_name_plural = "settings"
