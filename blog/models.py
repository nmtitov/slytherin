from django.db import models
from django.template.defaultfilters import slugify
from os import path as op
from bs4 import BeautifulSoup as Soup
from django.core.exceptions import ObjectDoesNotExist
from django.template import Template, Context


class Section(models.Model):
    title = models.CharField(max_length=32, unique=True)


class Post(models.Model):
    published = models.BooleanField(default=False, db_index=True)
    preview = models.BooleanField(default=False, db_index=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    thumbnail_image = models.OneToOneField('Image', related_name='thumbnail_image', blank=True, null=True, unique=False)
    slug = models.CharField(max_length=1024, db_index=True, null=False, unique=True)
    title_before = models.CharField(max_length=1024, blank=True)
    title = models.CharField(max_length=1024)
    title_after = models.CharField(max_length=1024, blank=True)
    verbose_title = models.CharField(max_length=1024)
    lead = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    compiled_body = models.TextField(blank=True, null=True, editable=False)
    side = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)

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

    @property
    def title_before_f(self):
        return self.title_before + " " if self.title_before else ""

    @property
    def title_after_f(self):
        return " " + self.title_after if self.title_after else ""

    def __str__(self):
        return "%s (%s)" % (self.title, self.title_before_f + self.title + self.title_after_f)


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


class Settings(models.Model):
    blog_title = models.CharField(max_length=1024)
    blog_copyright = models.CharField(max_length=1024)
    author_email = models.EmailField(max_length=254)
    counter_yandex_metrika = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.blog_title

    @classmethod
    def shared_instance(cls):
        if not cls.objects.exists():
            cls().save()
        return cls.objects.first()

    class Meta:
        verbose_name_plural = "settings"
