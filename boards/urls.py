from django.urls import path
from .views import board_lists, boards_page
urlpatterns = [
    path('lists/<int:board_id>',board_lists, name='lists'),
    path('boards_page/<int:project_id>', boards_page,name="boards_page")

]
