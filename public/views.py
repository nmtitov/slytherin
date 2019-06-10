from django.shortcuts import render
from django.http import Http404
from .models import Post, Section, Settings


def root(request):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_root()
        p = Post.list_by_section(s)
        settings = Settings.get()
        context = dict(sections=sections, section=s, root=r, posts=p, settings=settings)
        return render(request, 'public/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def posts(request, section: str):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_by_slug(section)
        p = Post.list_by_section(s)
        settings = Settings.get()
        context = dict(sections=sections, section=s, root=r, posts=p, settings=settings)
        return render(request, 'public/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def post(request, section_slug, post_slug):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_by_slug(section_slug)
        p = Post.get_by_section_and_slug(section=s, slug=post_slug)
        settings = Settings.get()
        context = dict(root=r, sections=sections, section=s, post=p, settings=settings)
        return render(request, 'public/post.html', context)
    except (Section.DoesNotExist, Post.DoesNotExist):
        raise Http404
