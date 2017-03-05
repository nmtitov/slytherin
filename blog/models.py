from django.db import models
from django.template.defaultfilters import slugify
from os import path as op
from bs4 import BeautifulSoup as Soup
from django.core.exceptions import ObjectDoesNotExist
from django.template import Template, Context
from typing import List, Type, TypeVar


S = TypeVar('S', bound='Section')
class Section(models.Model):
    title = models.CharField(max_length=32, unique=True)
    verbose_title = models.CharField(max_length=1024)
    slug = models.CharField(max_length=32, unique=True)

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
            if not self.slug:
                self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def section_html_id(self):
        return "page_{}".format(self.slug)

    def __str__(self):
        return self.title


P = TypeVar('P', bound='Post')
class Post(models.Model):
    section = models.ForeignKey(Section, related_name='posts', db_index=True, on_delete=models.PROTECT)
    draft = models.BooleanField(default=False, db_index=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    thumbnail_image = models.OneToOneField('Image', related_name='thumbnail_image', blank=True, null=True, unique=False)
    slug = models.CharField(max_length=1024, db_index=True, null=False, unique=True)
    title = models.CharField(max_length=1024)
    verbose_title = models.CharField(max_length=1024)
    lead = models.TextField(blank=True, null=True)
    body = models.TextField()
    compiled_body = models.TextField(blank=True, null=True, editable=False)
    side = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)

    @classmethod
    def list_by_section(cls: Type['P'], section: S) -> List[P]:
        return list(cls.objects.filter(section=section, draft=False).order_by('-publication_date'))

    @classmethod
    def get_by_section_and_slug(cls: Type['P'], section: S, slug: str) -> P:
        return Post.objects.get(section=section, slug=slug, draft=False)

    def compile(self):
        soup = Soup(self.body)
        for img in soup.find_all("img"):
            try:
                data_slug = img['data-slug']
                im = self.image_set.get(slug=data_slug)
                figure = Soup(im.figure_html)
                img.replaceWith(figure)
            except (KeyError, ObjectDoesNotExist) as e:
                pass
        self.compiled_body = str(soup)

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                self.slug = slugify(self.title)
        self.compile()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post)
    file = models.ImageField(upload_to="images")
    retina = models.BooleanField(default=False)
    slug = models.CharField(max_length=32, blank=True, null=True)
    alt = models.CharField(max_length=1024, blank=True, null=True)
    caption = models.CharField(max_length=1024, blank=True, null=True)
    figure_html_template_string = \
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
    figure_html_template = Template(figure_html_template_string)

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
        context = Context({'image': self})
        return self.figure_html_template.render(context)

    def save(self, *args, **kwargs):
        if not self.slug:
            n, e = op.splitext(op.basename(self.file.name))
            self.slug = n
        if not self.alt:
            self.alt = self.slug
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
