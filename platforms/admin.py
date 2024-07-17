from django.contrib import admin
from .models import Platform

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    '''
    Customises the Platform admin view to display, search and filter platforms
    '''
    list_display = ('name', 'developer', 'release_date')
    search_fields = ('name', 'developer')
    list_filter = ('release_date',)
