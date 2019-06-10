from django.db import models
from uuslug import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from .secton import Section


class Publication(models.Model):
    section = models.ForeignKey(Section, related_name='posts', db_index=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, db_index=True, unique=True, editable=False)
    # thumbnail_image = models.OneToOneField('Image', related_name='thumbnail_image', blank=True, null=True, unique=False)
    content = RichTextUploadingField()
    # side = RichTextField(blank=True, null=True)
    hidden = models.BooleanField(default=False, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True, editable=False)

    @classmethod
    def list_by_section(cls, section):
        return list(cls.objects.filter(section=section, hidden=False).order_by('-created_date'))

    @classmethod
    def get_by_section_and_slug(cls, section, slug: str):
        return Publication.objects.get(section=section, slug=slug, hidden=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, max_length=128, word_boundary=True, save_order=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title