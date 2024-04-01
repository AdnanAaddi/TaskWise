from django.urls import path
from .views import project_lists, add_list
urlpatterns = [
    path('lists/<int:project_id>',project_lists, name='boards'),
    path('add_list/<int:project_id>',add_list, name='add' ),
]
