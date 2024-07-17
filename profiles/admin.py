from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''
    Customises the Profile model admin view to display a list of fields, search and filters
    ''' 
    list_display = ('owner', 'created_at', 'updated_at', 'name')
    search_fields = ('owner__username', 'name')
    list_filter = ('created_at', 'updated_at', 'owner')
    

