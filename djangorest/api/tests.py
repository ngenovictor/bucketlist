from django.test import TestCase
from .models import BucketList
from rest_framework import status
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """
    This is the test suite for the BucketList Model Class
    """
    def setUp(self):
        """
        define test client and other variables
        """
        user = User.objects.create(username="victor")
        self.bucketlist_name = "Write world class code"
        self.bucketlist = BucketList(name=self.bucketlist_name, owner=user)

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
        user = User.objects.create(username="victor")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.bucketlist_data = {"name": "Go to Ibiza", "owner": user.id}
        self.response = self.client.post(
            reverse("create"),
            self.bucketlist_data,
            format="json"
        )

    def test_api_can_create_a_bucketlist(self):
        """
        test the api has bucketlist creation ability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """
        Test that the api can retrieve a particular bucketlist
        """
        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse("details", kwargs = {"pk": bucketlist.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_a_bucketlist(self):
        """
        Test the api can update the details of a bucketlist
        """
        bucketlist = BucketList.objects.get()
        change_bucketlist = {"name": "Be a universe class developer"}
        response = self.client.put(
            reverse("details", kwargs={"pk": bucketlist.id}),
            change_bucketlist,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_bucketlist(self):
        """
        test the api can delete a particular bucketlist
        """
        bucketlist = BucketList.objects.get()
        response = self.client.delete(
            reverse("details", kwargs={"pk": bucketlist.id}),
            format="json",
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
