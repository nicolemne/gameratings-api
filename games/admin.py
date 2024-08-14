from django.contrib import admin
from games.models import Game
from genres.models import Genre
from platforms.models import Platform
from .forms import GameForm


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """
    Customizes the Game admin view to display, search, and filter games.
    Uses autocomplete for Platform and Genre.
    """

    form = GameForm
    list_display = (
        "title",
        "game_developer",
        "platform",
        "genre",
        "average_star_rating",
        "multiplayer",
        "release_year_display",
    )
    search_fields = (
        "title",
        "game_developer",
        "platform__name",
        "genre__name",
        "release_year",
    )
    list_filter = ("platform", "genre", "multiplayer")
    autocomplete_fields = ["platform", "genre"]
    exclude = ("average_star_rating",)

    def release_year_display(self, obj):
        return obj.release_year.year if obj.release_year else "N/A"
