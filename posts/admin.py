from django.contrib import admin
from .models import Post
from .forms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customizes the Post admin view to display, search, and filter posts.
    """

    form = PostForm
    list_display = ("title", "owner", "game", "created_at", "updated_at", "star_rating")
    search_fields = ("title", "owner__username", "game__title")
    list_filter = ("created_at", "updated_at", "game", "owner", "star_rating")
