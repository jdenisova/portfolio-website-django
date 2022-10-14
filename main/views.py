from django.shortcuts import render
from django.http import HttpResponse

from .models import Project


def index(request):
    return render(request, 'main/index.html')


def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'main/portfolio.html', {'projects': projects})
