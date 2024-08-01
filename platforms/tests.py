from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Platform
from datetime import datetime
from django.utils.timezone import make_aware


class PlatformListViewTests(APITestCase):
    """
    Tests: Platform list view
    """

    def setUp(self):
        User.objects.create_user(username="nicole", password="blackcat")
        Platform.objects.create(
            name="Test Platform",
            developer="Test Developer",
            release_date=make_aware(datetime.now()),
        )

    def test_can_list_platforms(self):
        response = self.client.get("/platforms/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Test Platform")
        self.assertEqual(response.data["results"][0]["developer"], "Test Developer")
