from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)



class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return bool(obj.id == request.user or request.user.is_superuser)

class UserReadAccess(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in SAFE_METHODS and request.user.is_staff:
            return True

