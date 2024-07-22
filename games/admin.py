from django.contrib import admin
from games.models import Game
from genres.models import Genre
from platforms.models import Platform


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """
    Customizes the Game admin view to display, search, and filter games.
    Uses autocomplete for Platform and Genre.
    """

    list_display = (
        "title",
        "game_developer",
        "platform",
        "genre",
        "average_star_rating",
        "slug",
        "multiplayer",
    )
    search_fields = ("title", "game_developer", "platform__name", "genre__name")
    list_filter = ("platform", "genre", "multiplayer")
    autocomplete_fields = ["platform", "genre"]
    exclude = ("average_star_rating", "slug")
