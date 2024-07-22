from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Customises the Like admin view to display, search and filter likes
    """

    list_display = ("owner", "post", "created_at")
    search_fields = ("owner__username", "post__title")
    list_filter = ("created_at", "owner", "post")
