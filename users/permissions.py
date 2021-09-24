from rest_framework.permissions import BasePermission


class UserCreate(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.uuid == request.user.uuid or request.user.is_staff or request.user.is_superuser:
            return True
        return False
