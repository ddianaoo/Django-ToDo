from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        return False


class IsNotAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        return False


class IsSuperUserOrNotAuthenticate(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated or request.user.is_superuser:
            return True
        return False