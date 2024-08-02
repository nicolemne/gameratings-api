from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class SavedGame(models.Model):
    """
    Model to allow users to save a game to favourites.
    """

    STATUS_CHOICES = [
        ("wishlist", "Wishlist"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="saved_games"
    )
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="saved_by_users"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="wishlist"
    )

    class Meta:
        unique_together = ("user", "game")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} saved {self.game.title} to library"
