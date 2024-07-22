from django.contrib import admin
from .models import Platform
from .forms import PlatformForm


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    """
    Customizes the Platform admin view to display, search, and filter platforms.
    """

    form = PlatformForm
    list_display = ("name", "developer", "release_date")
    search_fields = ("name", "developer")
    list_filter = ("release_date",)
