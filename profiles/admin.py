from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''
    Customises the Profile admin view to display, search and filter profiles
    ''' 
    list_display = ('owner', 'created_at', 'updated_at', 'name')
    search_fields = ('owner__username', 'name')
    list_filter = ('created_at', 'updated_at', 'owner')
    

