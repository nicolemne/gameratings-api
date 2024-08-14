from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    star_rating = serializers.IntegerField()

    game_id = serializers.IntegerField()
    game_title = serializers.ReadOnlyField(source="game.title")
    game_platform = serializers.ReadOnlyField(source="game.platform.name")
    game_image = serializers.ImageField(source="game.image", read_only=True)
    game_developer = serializers.ReadOnlyField(source="game.game_developer")
    game_release_year = serializers.SerializerMethodField(source="game.release_year")
    game_genre = serializers.ReadOnlyField(source="game.genre.name")
    game_multiplayer = serializers.ReadOnlyField(source="game.multiplayer")
    game_average_star_rating = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size is larger than 2 MB")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096 px")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096 px")
        return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def get_game_release_year(self, obj):
        return obj.game.release_year.year if obj.game.release_year else "N/A"

    def get_game_average_star_rating(self, obj):
        if obj.game and hasattr(obj.game, "average_star_rating"):
            return round(obj.game.average_star_rating, 1)
        return None

    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "image_filter",
            "star_rating",
            "like_id",
            "likes_count",
            "comments_count",
            "game_id",
            "game_title",
            "game_platform",
            "game_image",
            "game_developer",
            "game_release_year",
            "game_genre",
            "game_multiplayer",
            "game_average_star_rating",
        ]
