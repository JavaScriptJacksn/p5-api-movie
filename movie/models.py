from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):

    title = models.CharField(max_length=255)
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movies_added"
    )
    plot = models.TextField(blank=True)
    runtime = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])

    CHOICES = (
        ("UNRATED", "Unrated"),
        ("TV-PG", "TV-PG"),
        ("TV-G", "TV-G"),
        ("TV-R", "TV-R"),
        ("TV-X", "TV-X")
    )

    rated = models.CharField(max_length=7, choices=CHOICES, default="UNRATED")
    poster = models.ImageField(
        upload_to='posters/', default='../default-poster_u5tci8.jpg'
    )
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2030)])
    lastupdated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
