from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from cv.models import Project
from django.shortcuts import render


def index(request):
    projects = Project.objects.order_by('-pub_date')
    context = {
        'projects': projects,
    }
    return render(request, 'cv/projects.html', context)

