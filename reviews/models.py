from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.body
