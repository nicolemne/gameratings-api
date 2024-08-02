from django import forms
from .models import Post
from django.core.validators import MaxValueValidator


class PostForm(forms.ModelForm):
    """
    Custom form for the Post model to only allow a maximum of 5 rating.
    """

    star_rating = forms.IntegerField(
        validators=[MaxValueValidator(5)],
        widget=forms.NumberInput(attrs={"max": 5, "min": 0}),
    )

    class Meta:
        model = Post
        fields = "__all__"
