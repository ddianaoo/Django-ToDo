from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *


def create_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            # только регистрация
            form.save()
            messages.success(request, 'You are successfully create account!')
            return redirect('signin')

            # регистрация и вход
            # user = form.save()
            # login(request, user)
            # messages.success(request, 'You are successfully create your account! You are logged in')
            # return redirect('home')
        else:
            messages.error(request, form.errors)
    else:
        form = UserAddForm()
    return render(request, 'myauth/create_user.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('lists')
        else:
            messages.error(request, 'Error happened! Please write correct data!')
    return render(request, 'myauth/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('home')



##################### REST

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAdminUser, ]
    serializer_class = UserSerializer


    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.order_by('-id').all()
        return []