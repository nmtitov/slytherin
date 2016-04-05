from django.contrib import admin
from blog.models import Section, Post, Image, Settings


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']


class ScreenshotInline(admin.StackedInline):
    model = Image
    extra = 4


@admin.register(Post)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ScreenshotInline]


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
