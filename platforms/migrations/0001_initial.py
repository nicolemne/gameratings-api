# Generated by Django 3.2.25 on 2024-07-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('developer', models.CharField(max_length=255)),
                ('release_date', models.DateTimeField()),
            ],
        ),
    ]
