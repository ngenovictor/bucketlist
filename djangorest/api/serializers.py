from rest_framework import serializers
from .models import BucketList


class BucketListSerializer(serializers.ModelSerializer):
    """
    serializer to map BucketList model to json format
    """
    class Meta:
        """
        to map serializer's fileds with model fields
        """
        model = BucketList
        fields = ("id", "name", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")
        