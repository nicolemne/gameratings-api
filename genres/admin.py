from django.contrib import admin
from .models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''
    Customizes the Genre admin view to display and search genres.
    '''
    list_display = ('name',)
    search_fields = ('name',)