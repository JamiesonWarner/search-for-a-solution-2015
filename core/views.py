from django.shortcuts import render, get_object_or_404
from .models import Project

def index(request):
  projects = Project.objects.prefetch_related('wanted_set').all()
  return render(request, 'index.html', { 'projects': projects })

def project_details(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'project_details.html', { 'project': project })
