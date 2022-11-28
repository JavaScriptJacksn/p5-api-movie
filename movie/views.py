from rest_framework.views import APIView
from django.db.models import Count
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from django.http.response import JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from movie_api.permissions import IsOwnerOrReadOnly


class MovieList(generics.ListCreateAPIView):
    """
    List all movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['title', 'rated', 'plot']
    ordering_fields = ['title', 'rated', 'plot', 'year']


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View details of one movie
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
