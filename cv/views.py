from django.shortcuts import render
from django.http import Http404
from cv.models import Project


def object_list(request, model):
    xs = model.objects.filter(published=True).order_by('-pub_date')
    template_name = 'cv/%s_list.html' % model.__name__.lower()
    return render(request, template_name, {'object_list': xs})


def detail(request, project_slug=None):
    try:
        x = Project.objects.filter(published=True).get(slug=project_slug)
    except Project.DoesNotExist:
        raise Http404
    context = dict(project=x)
    return render(request, 'cv/detail.html', context)


def plaintext_projects(request):
    xs = Project.objects.filter(published=True).order_by('-pub_date')
    return render(request, 'cv/plaintext_projects.html', dict(projects=xs))
