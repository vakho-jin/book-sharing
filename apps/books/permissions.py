from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """რედაქტირების უფლებას აძლევს მხოლოდ მფლობელს"""

    def has_object_permission(self, request, view, obj):
        # წაკითხვის უფლება აქვს სხვა ნებისმიერ რექუესთს (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user