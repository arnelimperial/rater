from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Rating
from . import serializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer


