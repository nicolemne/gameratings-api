from django import forms
from .models import Platform

class PlatformForm(forms.ModelForm):
    '''
    Override the release_date field to use a DateInput widget 
    to display only the date in the admin interface
    '''
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Platform
        fields = '__all__'
