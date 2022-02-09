from rest_framework import permissions


class IsOwnerOrContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser \
                or obj.author_user_id == request.user:
            return True
        if request.method == 'GET':
            if request.user in obj.contributors.all():
                return True
        return False


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser \
                or obj.author_user_id == request.user:
            return True
        return False
