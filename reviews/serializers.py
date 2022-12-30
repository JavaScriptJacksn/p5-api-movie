from rest_framework import serializers
from .models import Review
from movie.models import Movie


class ReviewSerializer(serializers.ModelSerializer):

    editor = serializers.ReadOnlyField(source='editor.username')

    class Meta:
        model = Review
        fields = [
            'id', 'movie', 'editor', 'created_on', 'updated_on', 'body',
            'rating',
        ]


class ReviewDetailSerializer(ReviewSerializer):
    movie = serializers.ReadOnlyField(source='movie.id')
