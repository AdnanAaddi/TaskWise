from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Board, Project, List

def project_lists(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Retrieve all lists associated with the project
    lists = List.objects.all()
    
    # You may want to further process the 'lists' queryset before returning it

    return HttpResponse(lists)

