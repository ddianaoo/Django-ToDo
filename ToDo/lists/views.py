from django.shortcuts import render


def get_lists(request):
    render(request, 'get_lists.html', {'title': 'My lists'})
