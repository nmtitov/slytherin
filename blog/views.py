from django.shortcuts import render
from django.http import Http404
from blog.models import Section, Post, Settings


def posts(request, section_slug):
    try:
        section = Section.get_by_slug(section_slug)
        xs = Post.list_by_section(section)
        settings = Settings.get()
        context = dict(section=section, posts=xs, settings=settings)
        return render(request, 'blog/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def post(request, section_slug, slug):
    try:
        section = Section.get_by_slug(section_slug)
        x = Post.get_by_section_and_slug(section=section, slug=slug)
        settings = Settings.get()
        context = dict(section=section, post=x, settings=settings)
        return render(request, 'blog/post.html', context)
    except (Section.DoesNotExist, Post.DoesNotExist):
        raise Http404
