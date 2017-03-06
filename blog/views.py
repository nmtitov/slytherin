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
        context = dict(sections=sections, section=s, root=r, publications=p, settings=settings)
        return render(request, 'blog/publications.html', context)
    except Section.DoesNotExist:
        raise Http404


def publications(request, section: str):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_by_slug(section)
        p = Publication.list_by_section(s)
        settings = Settings.get()
        context = dict(sections=sections, section=s, root=r, publications=p, settings=settings)
        return render(request, 'blog/publications.html', context)
    except Section.DoesNotExist:
        raise Http404


def publication(request, section, publication):
    try:
        r = Section.get_root()
        sections = Section.list()
        s = Section.get_by_slug(section)
        p = Publication.get_by_section_and_slug(section=s, slug=publication)
        settings = Settings.get()
        context = dict(root=r, sections=sections, section=s, publication=p, settings=settings)
        return render(request, 'blog/publication.html', context)
    except (Section.DoesNotExist, Publication.DoesNotExist):
        raise Http404
