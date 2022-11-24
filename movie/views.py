from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
from django.http.response import JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class MovieList(generics.ListCreateAPIView):
    """
    List all movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['title', 'rated', 'plot']
    ordering_fields = ['title', 'rated', 'plot', 'year']


class MovieDetail(generics.RetrieveAPIView):
    """
    View details of one movie
    """
    serializer_class = MovieSerializer

    def get_object(self, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            return movie
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(
            movie, context={'request': request}
        )

        # Add reviews to this response

        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
