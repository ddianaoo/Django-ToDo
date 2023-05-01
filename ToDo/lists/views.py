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
        form = TaskForm(request.POST, request.FILES, initial={'list': id})
        if form.is_valid():
            form.save()
            messages.success(request, 'New task was successfully created!')
        return redirect('tasks', id)
    else:
        form = TaskForm(initial={'list': id})
        return render(request, 'lists/task_create.html', {'form': form})


def task_details(request, list_id, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except:
        messages.error(request, 'You haven`t added this task yet!')
        return redirect('tasks', id)

    return render(request, 'lists/task_detail.html', {'task': task, 'list_id': list_id})


def change_task(request, list_id, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        form = ChangeTaskForm(request.POST, request.FILES, initial={'title': task.title, 'is_done': task.is_done, 'list': task.list}, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task', list_id, task_id)
        else:
            messages.error(request, form.errors)
    form = ChangeTaskForm(initial={'title': task.title, 'is_done': task.is_done, 'list': task.list}, instance=task)
    return render(request, 'lists/change_task.html', {'form': form, 'list_id': list_id})


def delete_task(request, list_id, task_id):

    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except:
        messages.error(request, 'Lose to delete this task!')
    else:
        messages.success(request, 'Task was successfully deleted!')
    return redirect('tasks', list_id)