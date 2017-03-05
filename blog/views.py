from django.shortcuts import render
from django.http import Http404
from blog.models import Section, Post, Settings
from django.db.models import Q


def posts(request, section_slug):
    try:
        section = Section.get_by_slug(section_slug)
        xs = Post.objects.filter(section=section, draft=False).order_by('-publication_date')
        settings = Settings.shared_instance()
        context = dict(section=section, posts=xs, settings=settings)
        return render(request, 'blog/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def post(request, section_slug, slug):
    try:
        section = Section.objects.get(slug=section_slug)
        x = Post.objects.get(slug=slug, draft=False)
        settings = Settings.shared_instance()
        context = dict(section=section, post=x, settings=settings)
        return render(request, 'blog/post.html', context)
    except (Section.DoesNotExist, Post.DoesNotExist):
        raise Http404
