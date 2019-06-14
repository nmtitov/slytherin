from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from project import local_settings


# Admin site configuration
admin.site.site_title = local_settings.admin_site_site_title
admin.site.site_header = local_settings.admin_site_site_header
admin.site.index_title = local_settings.admin_site_index_title

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('public.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
