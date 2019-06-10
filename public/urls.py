from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root, name='root'),
    url(r'^(?P<section>[A-Za-z0-9_-]+)/$', views.posts, name='posts'),
    url(r'^(?P<section_slug>[A-Za-z0-9_-]+)/(?P<post_slug>[A-Za-z0-9_-]+)/$', views.post, name='post'),
]