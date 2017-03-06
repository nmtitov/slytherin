from django import template
from blog.models import Publication, Section

register = template.Library()


@register.filter
def active_if(section: Section, active_slug):
    return "active" if section.slug == active_slug else ""
