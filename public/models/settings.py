from django.db import models


class Settings(models.Model):
    blog_title = models.CharField(max_length=1024)
    footer = models.TextField(blank=True, null=True)

    @classmethod
    def get(cls):
        return cls.objects.first()

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name_plural = "settings"
