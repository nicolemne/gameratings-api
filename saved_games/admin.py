from django.contrib import admin
from .models import SavedGame


@admin.register(SavedGame)
class SavedGameAdmin(admin.ModelAdmin):
    """
    Customizes the SavedGame admin view to display, search,
    and filter saved games
    """

    list_display = ("owner", "game", "status", "created_at")
    search_fields = ("owner__username", "game__title", "status")
    list_filter = ("status", "created_at", "owner", "game")
