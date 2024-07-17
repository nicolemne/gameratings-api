from rest_framework import serializers
from django.db import IntegrityError
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Platform model
    """
    # average_star_rating = serializers.ReadOnlyField()
    # slug = serializers.ReadOnlyField()

    class Meta:
        model = Genre
        fields = [
            'id', 'name'
        ]