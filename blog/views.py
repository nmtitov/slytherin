from django.shortcuts import render
from django.http import Http404
from blog.models import Post, Settings
from django.db.models import Q

def posts(request):
    template_name = "blog/posts.html"
    if request.user.is_staff:
        xs = Post.objects.filter(Q(published=True) | Q(preview=True)).order_by('-publication_date')
    else:
        xs = Post.objects.filter(published=True).order_by('-publication_date')
    settings = Settings.shared_instance()
    context = dict(posts=xs, settings=settings)
    return render(request, template_name, context)


def post(request, slug=None):
    template_name = 'blog/post.html'
    try:
        if request.user.is_staff:
            x = Post.objects.get(slug=slug).filter(Q(published=True) | Q(preview=True))
        else:
            x = Post.objects.get(slug=slug).filter(published=True)
    except Post.DoesNotExist:
        raise Http404
    settings = Settings.shared_instance()
    context = dict(post=x, settings=settings)
    return render(request, template_name, context)
