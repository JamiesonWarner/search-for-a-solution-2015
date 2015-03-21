from django.shortcuts import render
from .models import Project

def index(request):
  projects = Project.objects.prefetch_related('wanted_set').all()
  return render(request, 'index.html', { 'projects': projects })
