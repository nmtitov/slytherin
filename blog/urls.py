from django.conf.urls import url
from blog import views

urlpatterns = [
    # url(r'^$', views.posts, name='posts', kwargs={'section_slug': 'production'}),
    url(r'^$', views.root, name='root'),
    url(r'^(?P<section>[A-Za-z0-9_-]+)/$', views.posts, name='posts'),
    url(r'^(?P<section>[A-Za-z0-9_-]+)/(?P<post>[A-Za-z0-9_-]+)/$', views.post, name='post'),

    # url(r'^tutorials$', views.posts, name='tutorials', kwargs={'section_slug': 'tutorials'}),
    # url(r'^tutorials/(?P<slug>[A-Za-z0-9_-]+)/$', views.post, name='tutorials_object', kwargs={'section_slug': 'tutorials'}),
]