from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Customises the Comment admin view to display, search and filter comments
    """

    list_display = ("owner", "post", "created_at", "content")
    search_fields = ("owner__username", "post__title", "content")
    list_filter = ("created_at", "updated_at", "owner", "post")
