from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


admin.site.site_header = 'Sitename'

# Text to put at the end of each page's <title>.
admin.site.site_title = 'Sitename slytherin admin'

# Text to put in each page's <h1>.
admin.site.site_header = 'Sitename'

# Text to put at the top of the admin index page.
admin.site.index_title = 'Sitename administration'

urlpatterns = [
    path('^admin/', admin.site.urls),
    path('^ckeditor/', include('ckeditor_uploader.urls')),
    path('^', include('slytherin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
