from django.test import TestCase
from .models import BucketList


class ModelTestCase(TestCase):
    """
    This is the test suite for the BucketList Model Class
    """
    def setUp(self):
        """
        define test client and other variables
        """
        self.bucketlist_name = "Write world class code"
        self.bucketlist = BucketList(name = self.bucketlist_name)
    def test_model_can_create_a_bucket_list(self):
        """
        Test that the bucketlist model can create a bucketlist
        """
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count,new_count, "New count and Old count should not be equal")