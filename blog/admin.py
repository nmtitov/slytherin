from django.contrib import admin
from blog.models import Post, Image, Settings


class ScreenshotInline(admin.StackedInline):
    model = Image
    extra = 4


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ScreenshotInline]


admin.site.register(Post, ProjectAdmin)


class SettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Settings, SettingsAdmin)
