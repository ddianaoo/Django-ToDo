from django import forms
from .models import *


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ['title', 'user', 'invite', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'desc', 'list', 'photo', 'at_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'at_time': forms.TimeInput(attrs={'class': 'form-control'}),
        }


class ChangeTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'desc', 'is_done', 'list', 'photo', 'at_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'at_time': forms.TimeInput(attrs={'class': 'form-control'}),
        }