from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import SavedGame
from games.models import Game
from platforms.models import Platform
from genres.models import Genre
from datetime import datetime
from django.utils.timezone import make_aware


class SavedGameListViewTests(APITestCase):
    """
    Tests: SavedGame list view
    """

    def setUp(self):
        self.nicole = User.objects.create_user(username="nicole", password="blackcat")
        self.daniel = User.objects.create_user(username="daniel", password="purplegiraffe")
        platform = Platform.objects.create(
            name="Test Platform",
            developer="Test Developer",
            release_date=make_aware(datetime.now()),
        )
        genre = Genre.objects.create(name="Test Genre")
        game = Game.objects.create(
            title="Test Game",
            game_developer="Test Game Developer",
            platform=platform,
            genre=genre,
        )
        SavedGame.objects.create(
            user=self.nicole,
            game=game,
            status="wishlist",
        )

    def test_can_list_saved_games(self):
        self.client.login(username="nicole", password="blackcat")
        response = self.client.get("/saved_games/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["game_title"], "Test Game")
        self.assertEqual(response.data["results"][0]["status"], "wishlist")


class SavedGameDetailViewTests(APITestCase):
    """
    Tests: SavedGame detail view
    """

    def setUp(self):
        self.nicole = User.objects.create_user(username="nicole", password="blackcat")
        self.daniel = User.objects.create_user(username="daniel", password="purplegiraffe")
        platform = Platform.objects.create(
            name="Test Platform",
            developer="Test Developer",
            release_date=make_aware(datetime.now()),
        )
        genre = Genre.objects.create(name="Test Genre")
        self.saved_game_1 = SavedGame.objects.create(
            user=self.nicole,
            game=Game.objects.create(
                title="Nicole's Game",
                game_developer="Test Game Developer",
                platform=platform,
                genre=genre,
            ),
            status="wishlist",
        )
        self.saved_game_2 = SavedGame.objects.create(
            user=self.daniel,
            game=Game.objects.create(
                title="Daniel's Game",
                game_developer="Test Game Developer 2",
                platform=platform,
                genre=genre,
            ),
            status="in_progress",
        )

    def test_can_retrieve_saved_game_using_valid_id(self):
        self.client.login(username="nicole", password="blackcat")
        response = self.client.get(f"/saved_games/{self.saved_game_1.id}/")
        self.assertEqual(response.data["game_title"], "Nicole's Game")
        self.assertEqual(response.data["status"], "wishlist")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_saved_game_using_invalid_id(self):
        self.client.login(username="nicole", password="blackcat")
        response = self.client.get("/saved_games/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
