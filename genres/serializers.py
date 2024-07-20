from rest_framework import serializers
from django.db import IntegrityError
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Genre model
    """
    class Meta:
        model = Genre
        fields = [
            'id', 'name'
        ]