from rest_framework import permissions
from .models import *
from django.shortcuts import get_object_or_404


class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False


class IsListOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        my_url = request.META['PATH_INFO'].split('/')
        if len(my_url) == 6:
            list_id = my_url[-3]
        else:
            list_id = my_url[-2]
        my_list = get_object_or_404(List, id=int(list_id))
        if request.user.is_authenticated and my_list.id == request.user.id:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.user.id == request.user.id:
            return True
        return False


class IsTaskOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.list.user.id == request.user.id:
            return True
        return False