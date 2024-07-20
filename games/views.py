from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from gameratings.permissions import IsAdminOrOwnerOrReadOnly
from .models import Game
from .serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """
    List games or add a game when creating a post, if logged in.
    Uses django-filters to allow filtering by game developer, genre, platform, 
    and multiplayer. Supports ordering by posts count, unique reviewers count, 
    average star rating, game developer, genre, and platform.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.annotate(
        posts_count=Count('posts', distinct=True),
        unique_reviewers_count=Count('posts__owner', distinct=True),
    )
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'title',
        'game_developer',
        'genre__name',
        'platform__name',
        'multiplayer',
    ]
    filterset_fields = [
        'game_developer',
        'genre',
        'platform',
        'multiplayer'
    ]
    ordering_fields = [
        'posts_count',
        'unique_reviewers_count',
        'average_star_rating',
        'game_developer',
        'genre',
        'platform',
    ]
    

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a game instance. Only admins can delete
    a game instance.
    """
    permission_classes = [IsAdminOrOwnerOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.annotate(
        posts_count=Count('posts', distinct=True),
        unique_reviewers_count=Count('posts__owner', distinct=True),
    )
    lookup_field = 'slug'