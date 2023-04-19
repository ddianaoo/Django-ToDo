from django import forms
from .models import *


class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ['title', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }