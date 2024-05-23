from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Sets permission so that only the profile owner can
    make a PUT or PATCH request to its own profile. 
    All users can send GET requests to retrieve.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user