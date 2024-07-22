from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    """
    Customises the Follower admin view to display, search and filter followers
    """

    list_display = ("owner", "followed", "created_at")
    search_fields = ("owner__username", "followed__username")
    list_filter = ("created_at", "owner", "followed")
