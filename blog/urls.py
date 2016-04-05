from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^projects$', views.posts),
    url(r'^tutorials$', views.posts, name='tutorials', kwargs={'section_slug': 'tutorials'}),
    url(r'^projects/(?P<slug>[A-Za-z0-9_-]+)/$', views.post, name='post'),
    url(r'^tutorials/(?P<slug>[A-Za-z0-9_-]+)/$', views.post, name='tutorial', kwargs={'section_slug': 'tutorials'}),
]