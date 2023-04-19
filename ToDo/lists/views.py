from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView


def index(request):
    pass

def get_lists(request):
    lists = List.objects.all()
    return render(request, 'lists/get_lists.html', {'title': 'My notes', 'lists': lists})


def list_delete(request, id):
    list = List.objects.get(pk=id)
    list.delete()
    return redirect('lists')


# class AddNews(CreateView):
#     form_class = ListForm
#     template_name = 'lists/list_create.html'

def list_create(request):
    # user = request.user
    # user = user.id
    if request.method == 'POST':
        print(request.POST)
        form = ListForm(request.POST, initial={'user': 1 })
        if form.is_valid():
            form.save()
            return redirect('lists')
        else:
            print('Error')
    else:
        form = ListForm(initial={'user': 1})
    return render(request, 'lists/list_create.html', {'form': form})


def get_tasks(request, id):
    tasks = Task.objects.filter(list__id=id)
    return render(request, 'lists/get_tasks.html', {'title': 'My tasks', 'tasks': tasks})
