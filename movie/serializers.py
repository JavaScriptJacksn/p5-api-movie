from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    editor = serializers.ReadOnlyField(source='editor.username')

    class Meta:
        model = Movie
        fields = [
            'id', 'editor', 'plot', 'runtime', 'rated', 'poster',
            'title', 'year', 'lastupdated'
        ]
