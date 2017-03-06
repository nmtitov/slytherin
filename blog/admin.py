from django.contrib import admin
from blog.models import Section, Post, Image, Settings


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']


class ImageInline(admin.StackedInline):
    model = Image
    extra = 4


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
