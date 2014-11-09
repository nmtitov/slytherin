from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from cv.models import Project
from django.shortcuts import render


def index(request):
    projects = Project.objects.filter(published=True).order_by('-pub_date')
    context = {
        'projects': projects,
    }
    return render(request, 'cv/index.html', context)


def detail(request, project_slug=None):
    try:
        project = Project.objects.filter(published=True).get(slug=project_slug)
    except Project.DoesNotExist:
        raise Http404
    return render(request, 'cv/detail.html', {'project': project})


def projects(request):
    xs = Project.objects.filter(published=True).order_by('-pub_date')
    return render(request, 'cv/plaintext_projects.html', dict(projects=xs))
