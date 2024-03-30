from django.urls import path
from projects.views import create_project, display_projects, update_project,board
urlpatterns = [
    path('createproject/', create_project, name="createproject"),
    path('updateproject/<int:project_id>/update/', update_project, name='updateproject'),
     path('create-board/', board, name="board")
]
