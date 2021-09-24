from rest_framework.permissions import BasePermission


class LikeReadOrCreate(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user or request.user.is_staff:
            return True
        return False


class PostCreate(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.uuid == request.user.uuid or request.user.is_staff or request.user.is_superuser:
            return True
        return False
