from django.contrib import admin
from .models import Post, Section, Settings


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Post)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'created_date', 'release_date', )
    list_filter = ('section', 'created_date', 'release_date', )


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
