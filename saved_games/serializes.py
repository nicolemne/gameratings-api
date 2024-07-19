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
        Validates that the game being saved is not already 
        in the users saved games library.
        """
        user = self.context['request'].user
        if SavedGame.objects.filter(
            user=user, game=data['game']
            ).exists():
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
