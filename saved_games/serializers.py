from rest_framework import serializers
from .models import SavedGame

class SavedGameSerializer(serializers.ModelSerializer):
    """
    Serializer for the SavedGame model
    """
    user = serializers.ReadOnlyField(source='user.username')
    game_title = serializers.ReadOnlyField(source='game.title')

    def validate(self, data):
        """
        Checks if the game is already saved in the user's library.
        The validation is only applied when saving a new game.
        """
        request = self.context.get('request')
        if request and request.method == 'POST':
            user = request.user
            if SavedGame.objects.filter(user=user, game=data['game']).exists():
                raise serializers.ValidationError(
                    'This game is already saved to your library'
                )
        return data
    
    class Meta:
        model = SavedGame
        fields = [
            'id', 'user', 'game', 'game_title', 
            'created_at', 'status'
        ]
