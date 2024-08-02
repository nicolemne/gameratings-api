from rest_framework import serializers
from django.db import IntegrityError
from .models import Platform


class PlatformSerializer(serializers.ModelSerializer):
    """
    Serializer for the Platform model
    """
    
    release_date = serializers.SerializerMethodField()
    
    def get_release_date_year(self, obj):
        return obj.release_date.year
    

    class Meta:
        model = Platform
        fields = ["id", "name", "developer", "release_date"]
