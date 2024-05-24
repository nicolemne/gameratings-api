from django.db import models

class Game(models.Model):
    """
    Game model that stores information about the games
    that are reviewed. 
    """
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('RPG', 'Role-Playing Game'),
        ('Strategy', 'Strategy'),
        ('Simulation', 'Simulation'),
        ('Sports', 'Sports'),
    ]

    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('PS4', 'PlayStation 4'),
        ('XBOX', 'Xbox One'),
        ('SWITCH', 'Nintendo Switch'),
    ]

    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    average_star_rating = models.FloatField(default=0.0)

    class Meta:
        unique_together = (
            'title', 'developer', 'genre', 'platform'
        )

    def __str__(self):
        return self.title
