from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Profile


class ProfileListViewTests(APITestCase):
    """
    Tests: Profile list view
    """

    def setUp(self):
        nicole = User.objects.create_user(username="nicole", password="blackcat")
        daniel = User.objects.create_user(username="daniel", password="purplegiraffe")

    def test_automatic_profile_creation_new_user(self):
        response = self.client.get("/profiles/")
        count = Profile.objects.count()
        self.assertEqual(count, 2)

    def test_list_profiles(self):
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    """
    Tests: Profile detail view
    """
    
    def setUp(self):
        nicole = User.objects.create_user(username="nicole", password="blackcat")
        daniel = User.objects.create_user(username="daniel", password="purplegiraffe")
        
    def test_no_retrieve_profile_with_invalid_id(self):
        response = self.client.get("/profiles/666/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_retrieve_profile_with_valid_id(self):
        response = self.client.get("/profiles/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)