from django.contrib import admin
from .models import Platform
from .forms import PlatformForm


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    """
    Customizes the Platform admin view to display, search, and filter platforms.
    """

    form = PlatformForm
    list_display = ("name", "developer", "release_date_display")
    search_fields = ("name", "developer", "release_date",)
    list_filter = ("name", "release_date", "developer",)

    def release_date_display(self, obj):
        return obj.release_date.year if obj.release_date else "N/A"
