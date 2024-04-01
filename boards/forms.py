from django import forms 
from .models import Comment, Card, List, Board 

class Boardform(forms.ModelForm):  
    class Meta:
        model = Board
        fields = ['title']


class BoardForm(forms.ModelForm):
    
    class Meta:
        model = Board
        fields = ['title']


class CardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = ['title', 'descripton', 'opened_by', 'assigned_to', 'label', 'list']

        widgets= {
            'assigned_to': forms.CheckboxSelectMultiple
            
        }


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']

