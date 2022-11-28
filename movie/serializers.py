from rest_framework import serializers
from .models import Movie
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):

    editor = serializers.ReadOnlyField(source='editor.username')
    is_editor = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_is_editor(self, obj):
        request = self.context['request']
        return request.user == obj.editor

    def get_reviews(self, obj):
        queryset = Review.objects.filter(movie=obj.id)
        return ReviewSerializer(queryset, many=True).data


    class Meta:
        model = Movie
        fields = [
            'id', 'editor', 'plot', 'runtime', 'rated', 'poster',
            'title', 'year', 'lastupdated', 'is_editor', 'reviews',
        ]
