from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    return render(request, 'home.html')


def get_lists(request):
    user = request.user
    lists = List.objects.filter(user__id=user.id)
    return render(request, 'lists/get_lists.html', {'title': 'My notes', 'lists': lists})


def list_delete(request, id):
    list = List.objects.get(pk=id)
    list.delete()
    return redirect('lists')


def list_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = ListForm(request.POST, initial={'user': request.user.id})
        if form.is_valid():
            form.save()
            return redirect('lists')
        else:
            print('Error')
    else:
        form = ListForm(initial={'user': request.user.id})
    return render(request, 'lists/list_create.html', {'form': form})


def get_tasks(request, id):
    tasks = Task.objects.filter(list__id=id)
    return render(request, 'lists/get_tasks.html', {'title': 'My tasks', 'tasks': tasks})
