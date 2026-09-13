from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.methos in permissions.SAFE_PERMISSIONS:
            return True

        return request.user == obj.user
