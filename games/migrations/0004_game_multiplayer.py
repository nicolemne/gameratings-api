# Generated by Django 3.2.25 on 2024-07-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_game_game_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='multiplayer',
            field=models.BooleanField(default=False),
        ),
    ]
