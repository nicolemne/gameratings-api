from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    '''
    Customises the Game admin view to display, search and filter games
    ''' 
    list_display = ('title', 'platform', 'genre', 'average_star_rating', 'slug')
    search_fields = ('title', 'platform__name', 'genre__name')
    list_filter = ('platform', 'genre')
    prepopulated_fields = {'slug': ('title',)}
