from django.shortcuts import render
from django.http import Http404
from blog.models import Section, Post, Settings
from django.db.models import Q


def posts(request, section_slug=None):
    section_slug = section_slug if section_slug else Section.DEFAULT_SLUG
    try:
        section = Section.objects.get(slug=section_slug)
    except Section.DoesNotExist:
        raise Http404
    template_name = "blog/posts.html"
    if request.user.is_staff:
        xs = Post.objects.filter(Q(section=section) & (Q(published=True) | Q(preview=True))).order_by('-publication_date')
    else:
        xs = Post.objects.filter(Q(section=section) & Q(published=True)).order_by('-publication_date')
    settings = Settings.shared_instance()
    context = dict(section=section, posts=xs, settings=settings)
    return render(request, template_name, context)


def post(request, section_slug=None, slug=None):
    section_slug = section_slug if section_slug else Section.DEFAULT_SLUG
    template_name = 'blog/post.html'
    try:
        section = Section.objects.get(slug=section_slug)
        if request.user.is_staff:
            x = Post.objects.get(Q(slug=slug) & (Q(published=True) | Q(preview=True)))
        else:
            x = Post.objects.get(slug=slug, published=True)
    except (Section.DoesNotExist, Post.DoesNotExist):
        raise Http404
    settings = Settings.shared_instance()
    context = dict(section=section, post=x, settings=settings)
    return render(request, template_name, context)
