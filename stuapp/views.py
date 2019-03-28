from django.shortcuts import render

# Create your views here.
from stuapp.models import Actor,Movie
from stuapp.serializers import ActorSerializer,MovieSerializer
from rest_framework.viewsets import ModelViewSet


class ActorListView(ModelViewSet):
    queryset = Actor.objects.all()

    serializer_class = ActorSerializer

class MovieListView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

