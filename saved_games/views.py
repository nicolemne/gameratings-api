from django.db.models import F
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "game__title",
        "game__game_developer",
        "game__genre",
        "game__platform",
        "game__multiplayer",
        "status",
    ]
    ordering_fields = [
        "created_at",
        "average_star_rating",
    ]

    def get_queryset(self):
        """
        This view returns a list of all the saved games
        for the currently logged in user.
        """
        return SavedGame.objects.filter(
            user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SavedGameDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SavedGameSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        This view should return the details of the saved game
        for the currently authenticated user.
        """
        return (
            SavedGame.objects.filter(user=self.request.user)
            .annotate(average_star_rating=F("game__average_star_rating"))
            .order_by("-created_at")
        )
