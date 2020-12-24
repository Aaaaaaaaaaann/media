from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Allow authors to change and delete only their entries."""

    def has_object_permission(self, request, view, obj):
        if obj.author.pk == request.user.pk:
            return True
        return False
