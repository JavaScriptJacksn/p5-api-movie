from django.shortcuts import render
from rest_framework import generics, permissions
from movie_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer


class ReviewList(generics.ListCreateAPIView):

    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        serializer.save(editor=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
