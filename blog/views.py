from django.shortcuts import render
from django.http import Http404
from blog.models import Section, Publication, Settings


def root(request):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_root()
        p = Publication.list_by_section(s)
        settings = Settings.get()
        context = dict(sections=sections, section=s, root=r, posts=p, settings=settings)
        return render(request, 'blog/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def posts(request, section: str):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_by_slug(section)
        p = Publication.list_by_section(s)
        settings = Settings.get()
        context = dict(sections=sections, section=s, root=r, posts=p, settings=settings)
        return render(request, 'blog/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def post(request, section, post):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_by_slug(section)
        p = Publication.get_by_section_and_slug(section=s, slug=post)
        settings = Settings.get()
        context = dict(root=r, sections=sections, section=s, post=p, settings=settings)
        return render(request, 'blog/post.html', context)
    except (Section.DoesNotExist, Publication.DoesNotExist):
        raise Http404
