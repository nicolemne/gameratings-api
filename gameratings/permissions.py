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


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners to edit,
    and only admins to delete. All users can send
    GET requests to retrieve. Checks if user is
    admin with user.is_staff.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == "DELETE":
            return request.user and request.user.is_staff

        if request.method in ["PUT", "PATCH"]:
            return obj.posts.filter(owner=request.user).exists()

        return False


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to view, edit,
    or delete their saved games.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
