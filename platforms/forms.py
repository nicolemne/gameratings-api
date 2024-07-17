from django import forms
from .models import Platform

class PlatformForm(forms.ModelForm):
    '''
    Override the release_date field to use a NumberInput widget 
    to display only the year in the admin interface
    '''
    release_date = forms.DateField(
        widget=forms.NumberInput(attrs={
            'type': 'number',  # HTML input type set to number
            'min': '1900',  # Minimum year
            'max': '2100',  # Maximum year
            'step': '1',  # Step for the input, allows only whole numbers
            'placeholder': 'YYYY'  # Placeholder text
        }),
        input_formats=['%Y']  # Only accept the year format
    )

    class Meta:
        model = Platform
        fields = '__all__'