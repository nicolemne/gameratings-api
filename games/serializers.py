from rest_framework import serializers
from django.db import IntegrityError
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for the Game model
    The create method handles the unique constraint on 
    'title', 'game_developer', 'genre', and 'platform'
    """
    average_star_rating = serializers.ReadOnlyField()
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'game_developer', 'genre',
            'platform', 'average_star_rating', 'slug'
        ]


class NewGameSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new game.
    """
    class Meta:
        model = Game
        fields = [
            'title', 'game_developer', 'genre', 'platform'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'A game with these details already exists.'
            })

    def validate_title(self, value):
        if len(value) > 255:
            raise serializers.ValidationError('Title length exceeds 255 characters')
        return value