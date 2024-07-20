from rest_framework import serializers
from django.db import IntegrityError
from .models import Game
from platforms.models import Platform
from genres.models import Genre
from platforms.serializers import PlatformSerializer
from genres.serializers import GenreSerializer
        

class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for the Game model
    The create method handles the unique constraint on 
    'title', 'game_developer', 'genre', and 'platform'
    """
    average_star_rating = serializers.ReadOnlyField()
    slug = serializers.ReadOnlyField()
    posts_count = serializers.ReadOnlyField()
    unique_reviewers_count = serializers.ReadOnlyField()
    platform = PlatformSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Game
        fields = [
            'id', 'title', 'game_developer', 'genre', 'platform', 
            'average_star_rating', 'slug', 'multiplayer',
            'posts_count', 'unique_reviewers_count',
        ]


class NewGameSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new game.
    """
    class Meta:
        model = Game
        fields = [
            'title', 'game_developer', 'genre', 'platform',
            'multiplayer'
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