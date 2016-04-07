from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.posts, name='production', kwargs={'section_slug': 'production'}),
    url(r'^production/(?P<slug>[A-Za-z0-9_-]+)/$', views.post, name='production_object', kwargs={'section_slug': 'production'}),

    url(r'^tutorials$', views.posts, name='tutorials', kwargs={'section_slug': 'tutorials'}),
    url(r'^tutorials/(?P<slug>[A-Za-z0-9_-]+)/$', views.post, name='tutorials_object', kwargs={'section_slug': 'tutorials'}),
]