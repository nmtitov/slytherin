from django.contrib import admin
from blog.models import Post, Screenshot, Settings


class ScreenshotInline(admin.StackedInline):
    model = Screenshot
    extra = 4


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ScreenshotInline]


admin.site.register(Post, ProjectAdmin)


class SettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Settings, SettingsAdmin)
