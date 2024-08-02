from django.db import models
from django.utils.timezone import now


class Platform(models.Model):
    name = models.CharField(max_length=255, unique=True)
    developer = models.CharField(max_length=255)
    release_date = models.DateField(default=now)

    def __str__(self):
        return self.name
