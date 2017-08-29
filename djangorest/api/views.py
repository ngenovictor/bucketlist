from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList


class CreateView(generics.ListCreateAPIView):
    """
    class defines the create behaviour of our rest Api
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        """
        save the post data when creating a new bucketlist
        """
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Defines the update and delete behaviour api of our api
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer