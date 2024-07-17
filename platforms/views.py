from rest_framework import generics, permissions
from gameratings.permissions import IsAdminOrOwnerOrReadOnly
from .models import Platform
from .serializers import PlatformSerializer


class PlatformList(generics.ListCreateAPIView):
    """
    List all platforms when creating a post, only if authenticated.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()