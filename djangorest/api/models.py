from django.db import models


class BucketList(models.Model):
    """
    Defines the specs for out bucketlist model
    """
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.User', related_name='bucketlists', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        returns human readable format of the model
        """
        return self.name