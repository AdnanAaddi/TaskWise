from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Board, Project, List

def project_lists(request, project_id):
    lists = List.objects.filter(board=project_id)
    return render(request,'boards/boards.html',{'lists':lists})