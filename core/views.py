from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework import generics
from .forms import ProjectForm
from .models import Project

def index(request):
  projects = Project.objects.prefetch_related('wanted_set').all()
  return render(request, 'index.html', { 'projects': projects })

def project_details(request, project_id):
  project = get_object_or_404(Project, pk=project_id)
  return render(request, 'project_details.html', { 'project': project })

def create_project(request):
  form = ProjectForm()
  if request.method == 'POST':
    seeking_designer = ('seeking_designer' in request.POST)
    seeking_developer = ('seeking_developer' in request.POST)
    seeking_business = ('seeking_business' in request.POST)
    project = Project(
      title=request.POST['title'],
      description=request.POST['description'],
      owner=request.POST['owner'],
      owner_role=request.POST['owner_role'],
      owner_email=request.POST['owner_email'],
    )
    try:
      project.full_clean()
      project.save()
      return redirect('/')
    except Exception as e:
      print e
      return redirect('/error')
  return render(request, 'create_project.html', { 'form': form })
