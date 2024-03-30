from django.urls import path
from projects.views import create_project, display_projects
urlpatterns = [
    path('createproject/', create_project, name="createproject"),
    path('displayprojects/',display_projects , name="displayprojects"),
]
