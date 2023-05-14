from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.db.models import Q


def index(request):
    return render(request, 'home.html')


#WORK WITH LISTS
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


def change_list(request, id):
    list = List.objects.get(pk=id)

    if request.method == 'POST':
        form = ChangeListForm(request.POST, initial={'title': list.title, 'user': list.user}, instance=list)
        if form.is_valid():
            form.save()
            return redirect('tasks', id)
        else:
            messages.error(request, form.errors)
    form = ChangeListForm(initial={'title': list.title, 'user': list.user}, instance=list)
    return render(request, 'lists/change_list.html', {'form': form})


#WORK WITH TASKS
def get_tasks(request, id):
    try:
        list = List.objects.get(pk=id)
        tasks = Task.objects.filter(list__id=id)
        title = list.title
    except:
        messages.error(request, 'You don`t have permission to get details about this list')
        return redirect('lists')
    else:
        return render(request, 'lists/get_tasks.html', {'list': list, 'tasks': tasks, 'id':id})


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
        form = ChangeTaskForm(request.POST, request.FILES, initial={'title': task.title, 'is_done': task.is_done, 'list': task.list, 'photo': task.photo, 'at_time': task.at_time}, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task', list_id, task_id)
        else:
            messages.error(request, form.errors)
    form = ChangeTaskForm(initial={'title': task.title, 'is_done': task.is_done, 'list': task.list, 'photo': task.photo, 'at_time': task.at_time}, instance=task)
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



##################       REST

from rest_framework import viewsets
from .serializers import ListSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner, IsNotAllowed


class ListViewSet(viewsets.ModelViewSet):
    #queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated,]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated, ]

        elif self.request.user.is_authenticated:

            if self.action == 'retrieve':
                self.permission_classes = [IsOwner | IsAdminUser]

            if self.action == 'update':
                self.permission_classes = [IsOwner | IsAdminUser]

            if self.action == 'destroy':
                self.permission_classes = [IsOwner | IsAdminUser]
        else:
            self.permission_classes = [IsNotAllowed, ]
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            return List.objects.all()
        elif self.request.user.is_authenticated:
            return List.objects.filter(user__id=self.request.user.id)
        return []


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-pk')
    serializer_class = TaskSerializer