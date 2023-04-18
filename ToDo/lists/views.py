from django.shortcuts import render
from .models import *


def get_lists(request):
    lists = List.objects.all()
    return render(request, 'lists/get_lists.html', {'title': 'My lists', 'lists': lists})
