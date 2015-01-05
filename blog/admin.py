from django.contrib import admin
from blog.models import Project, Screenshot, Settings


class ScreenshotInline(admin.StackedInline):
    model = Screenshot
    extra = 4


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ScreenshotInline]


admin.site.register(Project, ProjectAdmin)


class SettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Settings, SettingsAdmin)
