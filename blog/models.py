from django.db import models
from django.template.defaultfilters import slugify


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
    side = models.TextField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            if not self.slug:
                self.slug = self.slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post)
    file = models.ImageField(upload_to=IMAGES_DIR, blank=True, null=True)

    def url(self):
        return self.file.url

    def __str__(self):
        return self.url()


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
