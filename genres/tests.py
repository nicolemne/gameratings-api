from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Genre


class GenreListViewTests(APITestCase):
    """
    Tests: Genre list view
    """

    def setUp(self):
        User.objects.create_user(username="nicole", password="blackcat")
        Genre.objects.create(
            name="Test Genre",
        )

    def test_can_list_genres(self):
        response = self.client.get("/genres/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "Test Genre")
