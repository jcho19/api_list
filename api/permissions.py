from rest_framework import permissions

# Any request has read permissions.
# Only the owner of the category/api has write permissions.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user