from django.contrib import admin
from posts.models import Post
from games.models import Game

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''
    Customizes the Post admin view to display, search, and filter posts.
    '''
    list_display = ('title', 'owner', 'game', 'created_at', 'updated_at')
    search_fields = ('title', 'owner__username', 'game__title')
    list_filter = ('created_at', 'updated_at', 'game', 'owner')
    autocomplete_fields = ['game']