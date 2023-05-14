from rest_framework import permissions


class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False


class IsListOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
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