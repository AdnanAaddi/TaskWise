from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm , UpdateProjectForm
from projects.models import Project
from .models import Project



# Create your views here.
@login_required(login_url='/login/')
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            print(project.owner)
            project.save()
            return redirect('dashboard')  # Redirect to the dashboard after project creation
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

def display_projects(user):
    user_projects = Project.objects.filter(owner=user)
    return user_projects

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = UpdateProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/update_project.html', {'form': form, 'project': project})

def board(request):
    return render(request,"projects/board.html")