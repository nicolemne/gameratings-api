from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from games.models import Game


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    image_filter_choices = [
        ("_1977", "1977"),
        ("brannan", "Brannan"),
        ("earlybird", "Earlybird"),
        ("hudson", "Hudson"),
        ("inkwell", "Inkwell"),
        ("lofi", "Lo-Fi"),
        ("kelvin", "Kelvin"),
        ("normal", "Normal"),
        ("nashville", "Nashville"),
        ("rise", "Rise"),
        ("toaster", "Toaster"),
        ("valencia", "Valencia"),
        ("walden", "Walden"),
        ("xpro2", "X-pro II"),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="posts", default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="../default_post_xcacib", blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default="normal"
    )
    star_rating = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(5)]
    )

    def save(self, *args, **kwargs):
        if self.game and not self.game_image:
            self.game_image = self.game.image
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
