from django.conf.urls import url
from slytherin import views

urlpatterns = [
    url(r'^$', views.root, name='root'),
    url(r'^(?P<section>[A-Za-z0-9_-]+)/$', views.publications, name='publications'),
    url(r'^(?P<section>[A-Za-z0-9_-]+)/(?P<publication>[A-Za-z0-9_-]+)/$', views.publication, name='publication'),
]