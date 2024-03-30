from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description','collaborators']

class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'collaborators']