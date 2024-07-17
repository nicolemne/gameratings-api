from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''
    Customises the Post admin view to display, search and filter posts
    ''' 
    list_display = ('title', 'owner', 'game', 'created_at', 'updated_at')
    search_fields = ('title', 'owner__username', 'game__title')
    list_filter = ('created_at', 'updated_at', 'game', 'owner')