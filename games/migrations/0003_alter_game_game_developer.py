# Generated by Django 3.2.25 on 2024-07-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_game_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_developer',
            field=models.CharField(max_length=255),
        ),
    ]
