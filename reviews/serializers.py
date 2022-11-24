from rest_framework import serializers
from .models import Review
from movie.models import Movie


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            'id', 'movie', 'author', 'created_on', 'updated_on', 'body', 'rating'
        ]
