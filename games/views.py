from rest_framework import generics, permissions
from gameratings.permissions import IsAdminOrOwnerOrReadOnly
from .models import Game
from .serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """
    List games or add a game when creating a post, if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a game instance. Only admins can delete
    a game instance.
    """
    permission_classes = [IsAdminOrOwnerOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    lookup_field = 'slug'