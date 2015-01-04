from django.conf.urls import patterns, url
from blog import models


urlpatterns = patterns('blog.views',
    url(r'^$', 'object_list', {'model': models.Project}, name='projects'),
    url(r'^projects$', 'object_list', {'model': models.Project}),
    url(r'^projects/(?P<project_slug>[A-Za-z0-9_-]+)/$', 'detail', name='detail'),
    url(r'^posts$', 'object_list', {'model': models.Post}, name='posts'),
    url(r'^screencasts$', 'object_list', {'model': models.Screencast}, name='screencasts'),
)