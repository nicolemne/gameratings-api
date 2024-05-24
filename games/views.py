from rest_framework import generics, permissions
from gameratings.permissions import IsOwnerOrReadOnly
from .models import Game
from .serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """
    List games or add a game when creating a post, if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class GameDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a game instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()