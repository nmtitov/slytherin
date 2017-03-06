from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.site.site_header = 'Sitename'

# Text to put at the end of each page's <title>.
admin.site.site_title = 'Sitename site admin'

# Text to put in each page's <h1>.
admin.site.site_header = 'Sitename'

# Text to put at the top of the admin index page.
admin.site.index_title = 'Sitename administration'

urlpatterns = [
    url(r'^s/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
