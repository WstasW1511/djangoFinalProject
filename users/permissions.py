from rest_framework.permissions import BasePermission


class PostCreate(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.user.is_staff:
            return True
        return False
