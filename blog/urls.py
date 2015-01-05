from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'posts', name='posts'),
    url(r'^projects$', 'posts'),
    url(r'^projects/(?P<slug>[A-Za-z0-9_-]+)/$', 'post', name='post'),
)