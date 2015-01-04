from django.contrib import admin
from blog.models import Project, Screenshot


class ScreenshotInline(admin.StackedInline):
    model = Screenshot
    extra = 4


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ScreenshotInline]

admin.site.register(Project, ProjectAdmin)
