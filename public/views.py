from django.shortcuts import render
from django.http import Http404
from .models import Post, Section, Settings


def posts(request, section=None):
    try:
        # Get model objects
        section_object = Section.get_by_slug(section) if section else Section.get_home()
        posts_dict = Post.list_by_section_group_by_year(section=section_object)

        # Render template
        context = {
            "sections": Section.list(),
            "section": section_object,
            "posts_dict": posts_dict,
            "settings": Settings.get(),
        }
        return render(request, 'public/posts.html', context)
    except Section.DoesNotExist:
        raise Http404


def post(request, section, post):
    try:
        s = Section.get_by_slug(section)
        context = {
            "sections": Section.list(),
            "section": s,
            "post": Post.get_by_section_and_slug(section=s, slug=post),
            "settings": Settings.get(),
        }
        return render(request, 'public/post.html', context)
    except (Section.DoesNotExist, Post.DoesNotExist):
        raise Http404
