from rest_framework.permissions import BasePermission
from .models import BucketList

class IsOwner(BasePermission):
    """
    Custom permission to allow only owner to edit a bucketlist
    """
    def has_object_permission(self, request, view, obj):
        """
        :return true if permission is granted to bucketlist owner
        """
        if isinstance(obj, BucketList):
            return obj.owner == request.user
        return obj.owner == request.user