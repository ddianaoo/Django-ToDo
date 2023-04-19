from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # только регистрация
            form.save()
            return redirect('signin')

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('okey')
            return redirect('lists')
        else:
            print('Error')
    return render(request, 'myauth/signin.html')


def signout(request):
    logout(request)
    return redirect('home')

