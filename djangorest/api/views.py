from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList
from rest_framework import permissions
from .permissions import IsOwner


class CreateView(generics.ListCreateAPIView):
    """
    class defines the create behaviour of our rest Api
    Handles POST and GET methods of our api
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """
        save the post data when creating a new bucketlist
        """
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Defines the update and delete behaviour api of our api
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)