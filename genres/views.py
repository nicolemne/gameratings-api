from rest_framework import generics, permissions, filters
from gameratings.permissions import IsAdminOrOwnerOrReadOnly
from .models import Genre
from .serializers import GenreSerializer


class GenreList(generics.ListCreateAPIView):
    """
    List all genres when creating a post, only if authenticated.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'name',
    ]
    ordering_fields = [
        'name',
    ]