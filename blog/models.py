from django.db import models
from django.template.defaultfilters import slugify
from os import path as op
from bs4 import BeautifulSoup as Soup

IMAGES_DIR = "images"


class Post(models.Model):
    published = models.BooleanField(default=False, db_index=True)
    preview = models.BooleanField(default=False, db_index=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    thumbnail_image = models.OneToOneField('Image', related_name='thumbnail_image', blank=True, null=True, unique=False)
    slug = models.CharField(max_length=1024, db_index=True, null=False, unique=True)
    title = models.CharField(max_length=1024)
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
                image_model = self.image_set.get(slug=data_slug)
                img['src'] = image_model.url
                img['width'] = image_model.width
                img['height'] = image_model.height
                img['alt'] = image_model.alt
            except KeyError:
                pass
        self.compiled_body = str(soup)

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                self.slug = self.slugify(self.title)
        self.compile()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post)
    file = models.ImageField(upload_to=IMAGES_DIR)
    retina = models.BooleanField(default=False)
    slug = models.CharField(max_length=32, blank=True, null=True)
    alt = models.CharField(max_length=1024, blank=True, null=True)

    @property
    def height(self):
        return self.file.height // 2 if self.retina else self.file.height

    @property
    def width(self):
        return self.file.width // 2 if self.retina else self.file.width

    @property
    def url(self):
        return self.file.url

    def save(self, *args, **kwargs):
        if not self.slug:
            n, e = op.splitext(op.basename(self.file.name))
            self.slug = n
        if not self.alt:
            self.alt = self.slug
        super(Image, self).save(*args, **kwargs)

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
