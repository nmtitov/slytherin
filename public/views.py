from django.shortcuts import render
from django.http import Http404
from .models import Post, Section, Settings


def root(request):
    try:
        context = {
            "sections": Section.list(),
            "section": Section.get_root(),
            "posts": Post.list_by_section(Section.get_root()),
            "settings": Settings.get(),
        }
        return render(request, 'public/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def posts(request, section: str):
    try:
        s = Section.get_by_slug(section)
        context = {
            "sections": Section.list(),
            "section": s,
            "posts": Post.list_by_section(s),
            "settings": Settings.get(),
        }
        return render(request, 'public/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def post(request, section_slug, post_slug):
    try:
        s = Section.get_by_slug(section_slug)
        context = {
            "sections": Section.list(),
            "section": s,
            "post": Post.get_by_section_and_slug(section=s, slug=post_slug),
            "settings": Settings.get(),
        }
        return render(request, 'public/post.html', context)
    except (Section.DoesNotExist, Post.DoesNotExist):
        raise Http404
