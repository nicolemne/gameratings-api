from rest_framework import serializers
from django.db import IntegrityError
from .models import Platform


class PlatformSerializer(serializers.ModelSerializer):
    """
    Serializer for the Platform model
    """
    # average_star_rating = serializers.ReadOnlyField()
    # slug = serializers.ReadOnlyField()

    class Meta:
        model = Platform
        fields = [
            'id', 'name', 'developer', 'release_date'
        ]