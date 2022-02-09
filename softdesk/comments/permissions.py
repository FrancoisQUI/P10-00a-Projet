from rest_framework import permissions

from projects.models import Project


class IsProjectAuthorOrContributorAndIssueAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            project = Project.objects.get(id=view.kwargs['projects_pk'])
        except Project.DoesNotExist:
            return False

        if request.user.id == project.author_user_id_id:
            return True

        if request.user in project.contributors.all():
            return True

        return False

    def has_object_permission(self, request, view, obj):
        try:
            project = Project.objects.get(id=view.kwargs['projects_pk'])
        except Project.DoesNotExist:
            return False

        if request.user.is_superuser:
            return True

        if request.user.id == obj.author_user_id_id:
            return True

        if request.method == "GET":
            if request.user in project.contributors.all():
                return True

        return False


