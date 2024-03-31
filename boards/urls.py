from django.urls import path
from .views import project_lists
urlpatterns = [
    path('lists/<int:project_id>',project_lists, name='boards')
]
