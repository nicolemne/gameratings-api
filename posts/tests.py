from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from games.models import Game
from platforms.models import Platform
from genres.models import Genre
from datetime import datetime
from django.utils.timezone import make_aware


class PostListViewTests(APITestCase):
    """
    Tests: Post list view
    """
    def setUp(self):
        self.nicole = User.objects.create_user(username="nicole", password="blackcat")
        self.platform = Platform.objects.create(
            name="Test Platform",
            developer="Test Developer",
            release_date=make_aware(datetime.now()),
        )
        self.genre = Genre.objects.create(name="Test Genre")
        self.game = Game.objects.create(
            title="Test Game",
            game_developer="Test Game Developer",
            platform=self.platform,
            genre=self.genre,
        )
        Post.objects.create(
            owner=self.nicole,
            game=self.game,
            title="Test Post Title",
            content="Content 123",
        )

    def test_can_list_posts(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Test Post Title")
        self.assertEqual(response.data["results"][0]["content"], "Content 123")


class PostDetailViewTests(APITestCase):
    """
    Tests: Post detail view
    """
    def setUp(self):
        self.nicole = User.objects.create_user(username="nicole", password="blackcat")
        self.daniel = User.objects.create_user(
            username="daniel", password="purplegiraffe"
        )
        self.platform = Platform.objects.create(
            name="Test Platform",
            developer="Test Developer",
            release_date=make_aware(datetime.now()),
        )
        self.genre = Genre.objects.create(name="Test Genre")
        self.game = Game.objects.create(
            title="Test Game",
            game_developer="Test Developer",
            platform=self.platform,
            genre=self.genre,
        )
        Post.objects.create(
            owner=self.nicole,
            game=self.game,
            title="Nicole's Post",
            content="test content",
        )
        Post.objects.create(
            owner=self.daniel,
            game=self.game,
            title="Daniel's Post",
            content="test content",
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.data["title"], "Nicole's Post")
        self.assertEqual(response.data["content"], "test content")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get("/posts/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
