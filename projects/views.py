from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm
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