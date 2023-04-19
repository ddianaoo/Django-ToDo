from django.shortcuts import render
from .models import *


def get_lists(request):
    lists = List.objects.all()
    return render(request, 'lists/get_lists.html', {'title': 'My notes', 'lists': lists})


def get_tasks(request, id):
    tasks = Task.objects.filter(list__id=id)
    return render(request, 'lists/get_tasks.html', {'title': 'My tasks', 'tasks': tasks})
