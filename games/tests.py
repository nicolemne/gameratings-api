from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Game
from platforms.models import Platform
from genres.models import Genre
from datetime import datetime
from django.utils.timezone import make_aware


class GameListViewTests(APITestCase):
    """
    Tests: Game list view
    """

    def setUp(self):
        nicole = User.objects.create_user(username="nicole", password="blackcat")
        daniel = User.objects.create_user(username="daniel", password="purplegiraffe")
        platform = Platform.objects.create(
            name="Test Platform",
            developer="Test Developer",
            release_date=make_aware(datetime.now()),
        )
        genre = Genre.objects.create(name="Test Genre")
        Game.objects.create(
            title="Test Game",
            game_developer="Test Game Developer",
            platform=platform,
            genre=genre,
        )

    def test_can_list_games(self):
        response = self.client.get("/games/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Test Game")
        self.assertEqual(
            response.data["results"][0]["game_developer"], "Test Game Developer"
        )


class GameDetailViewTests(APITestCase):
    """
    Tests: Game detail view
    """

    def setUp(self):
        nicole = User.objects.create_user(username="nicole", password="blackcat")
        daniel = User.objects.create_user(username="daniel", password="purplegiraffe")
        platform = Platform.objects.create(
            name="Test Platform",
            developer="Test Developer",
            release_date=make_aware(datetime.now()),
        )
        genre = Genre.objects.create(name="Test Genre")
        self.game_1 = Game.objects.create(
            title="Nicole's Game",
            game_developer="Test Game Developer",
            platform=platform,
            genre=genre,
        )
        self.game_2 = Game.objects.create(
            title="Daniel's Game",
            game_developer="Test Game Developer 2",
            platform=platform,
            genre=genre,
        )

    def test_can_retrieve_game_using_valid_slug(self):
        response = self.client.get(f"/games/{self.game_1.slug}/")
        self.assertEqual(response.data["title"], "Nicole's Game")
        self.assertEqual(response.data["game_developer"], "Test Game Developer")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_game_using_invalid_slug(self):
        response = self.client.get("/games/invalid-slug/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
