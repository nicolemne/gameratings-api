from rest_framework import generics, permissions, filters
from gameratings.permissions import IsAdminOrOwnerOrReadOnly
from .models import Platform
from .serializers import PlatformSerializer


class PlatformList(generics.ListCreateAPIView):
    """
    List all platforms when creating a post, only if authenticated.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PlatformSerializer
    pagination_class = None
    
    queryset = Platform.objects.all()
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "name",
        "developer",
    ]
    ordering_fields = [
        "name",
        "developer",
        "release_date",
    ]
