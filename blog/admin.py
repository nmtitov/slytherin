from django.contrib import admin
from blog.models import Post, Image, Settings


class ScreenshotInline(admin.StackedInline):
    model = Image
    extra = 4


@admin.register(Post)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ScreenshotInline]


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
