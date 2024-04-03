from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Board, Project, List
from django.urls import reverse

def boards_page(request, project_id):
    project = Project.objects.get(pk=project_id)
    boards = Board.objects.filter(project_id=project_id)

    if request.method == 'POST':
        board_name = request.POST.get('board_name')
        # Create a new board associated with the project
        new_board = Board.objects.create(project=project, title=board_name)
        List.objects.create(title='To Do', board=new_board)
        List.objects.create(title='Doing', board=new_board)
        List.objects.create(title='Completed', board=new_board)
        # Redirect the user back to the boards page after creating the board
        return redirect(reverse('boards_page', kwargs={'project_id': project_id}))
    return render(request, 'boards/boards.html', {'project': project, 'boards': boards})

def board_lists(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    
    if request.method == 'POST':
        # Handling the form submission for creating a new list
        list_title = request.POST.get('list_title')
        if list_title:  # Ensure the list title is not empty
            List.objects.create(board=board, title=list_title)
            # Redirect to the same page to display the updated list of lists and avoid form resubmission
            return redirect(reverse('lists', kwargs={'board_id': board_id}))

    # This part will execute for GET requests and also for POST if no redirect happens
    lists = List.objects.filter(board=board)  # Ordering by most recent
    return render(request, 'boards/lists.html', {'board': board, 'lists': lists})