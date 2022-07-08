from rest_framework.permissions import BasePermission

from users.models import User


def create_custom_action_permission(permission_class, actions=None):
    class Permission(permission_class):

        def has_permission(self, request, view):
            if actions and view.action not in actions:
                return True

            return super().has_permission(request, view)

        def has_object_permission(self, request, view, obj):
            if actions and view.action not in actions:
                return True

            return super().has_object_permission(request, view, obj)

    return Permission


class IsAuthenticatedOrAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return request.user.role == User.ADMIN

