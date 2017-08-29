from django.test import TestCase
from .models import BucketList
from rest_framework import status
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse


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


class ViewTestCase(TestCase):
    """
    Test suite for the api views
    """
    def setUp(self):
        """
        define test client and other variables
        """
        self.client = APIClient()
        self.bucketlis_data = {"name":"Go to Ibiza"}
        self.response = self.client.post(
            reverse("create"),
            self.bucketlis_data,
            format="json"
        )

    def test_api_can_create_a_bucketlist(self):
        """
        test the api has bucketlist creation ability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
