from django.db.models import F
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from gameratings.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import SavedGame
from .serializers import SavedGameSerializer


class SavedGameList(generics.ListCreateAPIView):
    """
    List saved games or add a game to the saved list if logged in.
    Uses django-filters to allow filtering by related game fields.
    """

    serializer_class = SavedGameSerializer
    permission_classes = [IsAuthenticated]
    queryset = SavedGame.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
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
    search_fields = [
        "status",
        "game__title",
        "game__game_developer",
        "game__genre__name",
        "game__platform__name",
        "game__release_year",
    ]

    def get_queryset(self):
        """
        This view returns a list of all the saved games
        for the currently logged in user.
        """
        return SavedGame.objects.filter(owner=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavedGameDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SavedGameSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        This view should return the details of the saved game
        for the currently authenticated user.
        """
        return SavedGame.objects.filter(owner=self.request.user).order_by("-created_at")
