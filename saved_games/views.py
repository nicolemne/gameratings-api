from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from gameratings.permissions import IsOwnerOrReadOnly
from .models import SavedGame
from .serializers import SavedGameSerializer


class SavedGameList(generics.ListCreateAPIView):
    """
    List saved games or add a game to the saved list if logged in.
    Uses django-filters to allow filtering by related game fields.
    """
    serializer_class = SavedGameSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = SavedGame.objects.all().order_by('-created_at')
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        'game__title',
        'game__game_developer',
        'game__genre',
        'game__platform',
        'game__multiplayer',
        'status',
    ]
    ordering_fields = [
        'created_at',
        'average_star_rating',
    ]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)