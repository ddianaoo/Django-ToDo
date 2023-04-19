from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


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
        #print(request.POST)
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
    tasks = Task.objects.filter(list__id=id)
    return render(request, 'lists/get_tasks.html', {'title': 'My tasks', 'tasks': tasks})
