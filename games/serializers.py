from rest_framework import serializers
from django.db import IntegrityError
from .models import Game
from platforms.models import Platform
from genres.models import Genre
from platforms.serializers import PlatformSerializer
from genres.serializers import GenreSerializer


class GameSerializer(serializers.ModelSerializer):
    """
    Combined Serializer for the Game model.
    Handles both creation and listing of games.
    """

    average_star_rating = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    unique_reviewers_count = serializers.ReadOnlyField()
    platform = PlatformSerializer(read_only=True)
    genre = GenreSerializer(read_only=True)
    image = serializers.ImageField(required=False, allow_null=True)
    release_year = serializers.SerializerMethodField()

    platform_id = serializers.PrimaryKeyRelatedField(
        queryset=Platform.objects.all(), write_only=True, source="platform"
    )
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), write_only=True, source="genre"
    )

    def validate_image(self, value):
        if value is None:
            return value

        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size is larger than 2 MB")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096 px")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096 px")
        return value

    def get_release_year(self, obj):
        return obj.release_year.year if obj.release_year else "N/A"

    def get_average_star_rating(self, obj):
        return round(obj.average_star_rating, 1)

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

    class Meta:
        model = Game
        fields = [
            "id",
            "title",
            "game_developer",
            "platform_id",
            "genre_id",
            "genre",
            "platform",
            "average_star_rating",
            "multiplayer",
            "image",
            "posts_count",
            "unique_reviewers_count",
            "release_year",
        ]
