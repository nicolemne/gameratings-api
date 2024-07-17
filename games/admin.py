from django.contrib import admin
from games.models import Game
from genres.models import Genre
from platforms.models import Platform

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    '''
    Customizes the Game admin view to display, search, and filter games.
    Uses autocomplete for Platform and Genre.
    '''
    list_display = ('title', 'platform', 'genre', 'average_star_rating', 'slug')
    search_fields = ('title', 'platform__name', 'genre__name')
    list_filter = ('platform', 'genre')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['platform', 'genre']
    exclude = ('average_star_rating',)
