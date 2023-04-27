from django import forms
from .models import *


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ['title', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'desc', 'list']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class ChangeTaskForm(forms.ModelForm):
    # title = models.CharField(max_length=150)
    # desc = models.TextField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # list = models.ForeignKey(List, on_delete=models.CASCADE, blank=False)
    # is_done = models.BooleanField(default=False)

    class Meta:
        model = Task
        fields = ['title', 'desc', 'is_done', 'list']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }