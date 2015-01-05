from django.shortcuts import render
from django.http import Http404
from blog.models import Project, Settings


def get_settings() -> Settings:
    return Settings.objects.first()


def object_list(request, model):
    xs = model.objects.filter(published=True).order_by('-pub_date')
    template_name = 'blog/%s_list.html' % model.__name__.lower()
    return render(request, template_name, {'object_list': xs, 'settings': get_settings()})


def detail(request, project_slug=None):
    try:
        x = Project.objects.filter(published=True).get(slug=project_slug)
    except Project.DoesNotExist:
        raise Http404
    context = dict(project=x)
    return render(request, 'blog/detail.html', context)
