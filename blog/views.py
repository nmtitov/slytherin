from django.shortcuts import render
from django.http import Http404
from blog.models import Post, Settings


def get_posts() -> list:
    Post.objects.filter(published=True).order_by('-pub_date')


def get_post(slug: str):
    return Post.objects.filter(published=True).get(slug=slug)


def posts(request):
    template_name = "blog/posts.html"
    return render(request, template_name, dict(posts=get_posts(), settings=Settings.shared_instance()))


def post(request, slug: str=None):
    try:
        p = get_post(slug)
    except Post.DoesNotExist:
        raise Http404
    context = dict(post=p)
    return render(request, 'blog/post.html', context)
