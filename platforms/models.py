from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=255, unique=True)
    developer = models.CharField(max_length=255)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.name