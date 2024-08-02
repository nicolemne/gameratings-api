from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    """
    Override the release_year field to use a NumberInput widget
    to display only the year in the admin interface
    """

    release_year = forms.DateField(
        widget=forms.NumberInput(
            attrs={
                "type": "number",
                "min": "1900",
                "max": "2100",
                "step": "1",
                "placeholder": "YYYY",
            }
        ),
        input_formats=["%Y"],
    )

    class Meta:
        model = Game
        fields = "__all__"
