from django.db import models
from os import path as op
from django.template import Template, Context
from uuslug import slugify
from .post import Post


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
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
