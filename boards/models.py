from django.db import models
from projects.models import Project

# Create your models here.

class Board(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name
    
    

    def add_list(self, list_name):
        new_list = List.objects.create(name=list_name, board=self)
        return new_list

class List(models.Model):
    tittle = models.CharField(max_length=100)
    board = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
    
