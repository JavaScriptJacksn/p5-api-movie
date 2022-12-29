from rest_framework import serializers
from .models import Review
from movie.models import Movie


class ReviewSerializer(serializers.ModelSerializer):

    editor = serializers.ReadOnlyField(source='editor.username')
    is_editor = serializers.SerializerMethodField()

    def get_is_editor(self, obj):
        request = self.context['request']
        return request.user == obj.editor


    class Meta:
        model = Review
        fields = [
            'id', 'movie', 'editor', 'created_on', 'updated_on', 'body', 'rating', 'is_editor'
        ]


class ReviewDetailSerializer(ReviewSerializer):
    movie = serializers.ReadOnlyField(source='movie.id')
