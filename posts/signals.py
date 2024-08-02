from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Post
from games.models import Game


@receiver(post_save, sender=Post)
@receiver(post_delete, sender=Post)
def update_average_star_rating(sender, instance, **kwargs):
    """
    Updates the average star rating of a game
    whenever a post is saved or deleted.
    """
    game = instance.game
    posts = Post.objects.filter(game=game)
    if posts.exists():
        average_rating = posts.aggregate(
            Avg("star_rating"))["star_rating__avg"]
        game.average_star_rating = average_rating
    else:
        game.average_star_rating = 0
    game.save()
