from django.urls import path
from . import views


app_name = 'public'

urlpatterns = [
    path("", views.posts, name="home"),
    path("<slug:section>/", views.posts, name="posts"),
    path("<slug:section>/<slug:post>/", views.post, name="post"),
]