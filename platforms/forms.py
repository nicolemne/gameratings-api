from django import forms
from .models import Platform

class PlatformForm(forms.ModelForm):
    '''
    Override the release_date field to use a NumberInput widget 
    to display only the year in the admin interface
    '''
    release_date = forms.DateField(
        widget=forms.NumberInput(attrs={
            'type': 'number', 'min': '1900', 'max': '2100', 'step': '1', 'placeholder': 'YYYY'
            }),
        input_formats=['%Y']
    )

    class Meta:
        model = Platform
        fields = '__all__'
