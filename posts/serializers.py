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
    game_title = serializers.ReadOnlyField(source="game.title")
    game_platform = serializers.ReadOnlyField(source="game.platform.name")
    game_image = serializers.ImageField(source="game.image", read_only=True)
    created_at = serializers.DateTimeField(format='%d %b %Y')
    updated_at = serializers.DateTimeField(format='%d %b %Y')

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
            "game_title",
            "game_platform",
            "game_image",
        ]
