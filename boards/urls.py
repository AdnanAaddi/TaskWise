from django.urls import path
from .views import board_lists, boards_page, add_card
urlpatterns = [
    path('lists/<int:board_id>',board_lists, name='lists'),
    path('boards_page/<int:project_id>', boards_page,name="boards_page"),
    path('add_card/<int:list_id>', add_card,name="add_card"),

]
