from django.db import models
from django.utils.text import slugify

class Game(models.Model):
    """
    Game model that stores information about the games
    that are reviewed. Generates a URL-slug from the title 
    and platform name.
    """
    title = models.CharField(max_length=255)
    game_developer = models.CharField(max_length=255)
    platform = models.ForeignKey(
        'platforms.Platform', on_delete=models.CASCADE, related_name='games'
        )
    genre = models.ForeignKey(
        'genres.Genre', on_delete=models.CASCADE, related_name='games'
        )
    average_star_rating = models.FloatField(default=0.0)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    multiplayer = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='images/', default='../gg_default_new_game_hiawpf', blank=True
    )

    class Meta:
        unique_together = (
            'title', 'genre', 'platform'
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title} {self.platform.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.platform.name})'
