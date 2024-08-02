from rest_framework import serializers
from django.db import IntegrityError
from .models import Platform


class PlatformSerializer(serializers.ModelSerializer):
    """
    Serializer for the Platform model
    """

    release_date = serializers.SerializerMethodField()

    def get_release_date(self, obj):
        return obj.release_date.year if obj.release_date else "N/A"

    class Meta:
        model = Platform
        fields = ["id", "name", "developer", "release_date"]
