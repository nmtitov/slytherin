from django.shortcuts import render
from django.http import Http404
from blog.models import Post, Settings


def posts(request):
    template_name = "blog/posts.html"
    xs = Post.objects.filter(published=True).order_by('-publication_date')
    context = dict(posts=xs, settings=Settings.shared_instance())
    return render(request, template_name, context)


def post(request, slug: str=None):
    template_name = 'blog/post.html'
    try:
        x = Post.objects.filter(published=True).get(slug=slug)
    except Post.DoesNotExist:
        raise Http404
    context = dict(post=x)
    return render(request, template_name, context)
