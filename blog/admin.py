from django.contrib import admin
from blog.models import Section, Publication, Image, Settings


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title']


# class ImageInline(admin.StackedInline):
#     model = Image
#     extra = 4


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    # inlines = [ImageInline]
    list_display = ('title', 'section', 'created_date', )
    list_filter = ('section', 'created_date', )


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass
