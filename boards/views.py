from django.shortcuts import render, HttpResponse, redirect
from .models import Board, Project, List
from django.urls import reverse

def boards_page(request, project_id):
    project = Project.objects.get(pk=project_id)
    boards = Board.objects.filter(project_id=project_id)

    if request.method == 'POST':
        # If the request is a POST request, it means the user is trying to add a new board
        board_name = request.POST.get('board_name')
        # Create a new board associated with the project
        new_board = Board.objects.create(project=project, title=board_name)
        # Redirect the user back to the boards page after creating the board
        return redirect(reverse('boards_page', kwargs={'project_id': project_id}))
    return render(request, 'boards/boards.html', {'project': project, 'boards': boards})

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
   

