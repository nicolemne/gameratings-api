from rest_framework import serializers
from .models import SavedGame


class SavedGameSerializer(serializers.ModelSerializer):
    """
    Serializer for the SavedGame model
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    game_id = serializers.IntegerField()
    game_title = serializers.ReadOnlyField(source="game.title")
    game_platform = serializers.ReadOnlyField(source="game.platform.name")
    game_image = serializers.ImageField(source="game.image", read_only=True)
    game_developer = serializers.ReadOnlyField(source="game.game_developer")
    game_release_year = serializers.SerializerMethodField(source="game.release_year")
    game_genre = serializers.ReadOnlyField(source="game.genre.name")
    game_multiplayer = serializers.ReadOnlyField(source="game.multiplayer")
    game_average_star_rating = serializers.SerializerMethodField()

    def validate(self, data):
        """
        Checks if the game is already saved in the user's library.
        The validation is only applied when saving a new game.
        """
        request = self.context.get("request")
        if request and request.method == "POST":
            owner = request.user
            if SavedGame.objects.filter(owner=owner, game=data["game"]).exists():
                raise serializers.ValidationError(
                    "This game is already saved to your library"
                )
        return data

    def get_game_release_year(self, obj):
        return obj.game.release_year.year if obj.game.release_year else "N/A"

    def get_game_average_star_rating(self, obj):
        if obj.game and hasattr(obj.game, "average_star_rating"):
            return round(obj.game.average_star_rating, 1)
        return None

    class Meta:
        model = SavedGame
        fields = [
            "id",
            "owner",
            "created_at",
            "status",
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
