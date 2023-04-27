from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'home.html')


def get_lists(request):
    user = request.user
    lists = List.objects.filter(user__id=user.id)
    return render(request, 'lists/get_lists.html', {'title': 'My notes', 'lists': lists})


def list_delete(request, id):
    try:
        list = List.objects.get(pk=id)
        list.delete()
    except:
        messages.error(request, 'Lose to delete this list!')
    else:
        messages.success(request, 'ToDo List was successfully deleted!')
    return redirect('lists')


def list_create(request):
    if request.method == 'POST':
        # print(request.POST)
        form = ListForm(request.POST, initial={'user': request.user.id})
        if form.is_valid():
            form.save()
            messages.success(request, 'ToDo List was successfully created!')
            return redirect('lists')
        else:
            messages.error(request, form.errors)
    else:
        form = ListForm(initial={'user': request.user.id})
    return render(request, 'lists/list_create.html', {'form': form})


def get_tasks(request, id):
    try:
        list = List.objects.get(pk=id)
        tasks = Task.objects.filter(list__id=id)
        title = list.title
    except:
        messages.error(request, 'You don`t have permission to get details about this list')
        return redirect('lists')
    else:
        return render(request, 'lists/get_tasks.html', {'title': title, 'tasks': tasks, 'id':id})


def add_task(request, id):
    if request.method == 'POST':
        form = TaskForm(request.POST, initial={'list': id})
        if form.is_valid():
            form.save()
            messages.success(request, 'New task was successfully created!')
        return redirect('tasks', id)
    else:
        form = TaskForm(initial={'list': id})
        return render(request, 'lists/task_create.html', {'form': form})
