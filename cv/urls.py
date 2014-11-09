from django.conf.urls import patterns, url

from cv import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project_slug>[A-Za-z0-9_-]+)/$', views.detail, name='detail'),
)