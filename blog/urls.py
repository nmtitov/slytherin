from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('blog.views',
    url(r'^$', views.posts, name='posts'),
    url(r'^projects$', views.posts),
    url(r'^projects/(?P<slug>[A-Za-z0-9_-]+)/$', views.post, name='post'),
)