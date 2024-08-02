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
    image = serializers.ImageField(required=False, allow_null=True)
    release_year = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size is larger than 2 MB")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096 px")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096 px")
        return value
    
    def get_release_year(self, obj):
        return obj.release_year.year if obj.release_year else "N/A"

    class Meta:
        model = Game
        fields = [
            "id",
            "title",
            "game_developer",
            "genre",
            "platform",
            "average_star_rating",
            "slug",
            "multiplayer",
            "image",
            "posts_count",
            "unique_reviewers_count",
            "release_year",
        ]


class NewGameSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new game.
    """

    class Meta:
        model = Game
        fields = [
            "title",
            "game_developer",
            "genre",
            "platform",
            "multiplayer",
            "image",
            "release_year",
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "A game with these details already exists."}
            )

    def validate_title(self, value):
        if len(value) > 255:
            raise serializers.ValidationError("Title length exceeds 255 characters")
        return value
