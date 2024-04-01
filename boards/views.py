from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Board, Project, List

def project_lists(request, project_id):
    lists = List.objects.filter(board=project_id)
    project = Project.objects.get(pk=project_id)
    context={
            'project': project,
            'lists':lists

    }
    return render(request,'boards/boards.html',context)

def add_list(request, project_id):
    project= Project.objects.all().filter(id=project_id)
    return render(request, 'boards/add_list.html')  
   

