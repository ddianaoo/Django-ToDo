from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # только регистрация
            form.save()
            return redirect('lists')

            # регистрация и вход
            # user = form.save()
            # login(request, user)
            # return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'myauth/create_user.html', {'form': form})


def signin(request):
    pass


def signout(request):
    pass


