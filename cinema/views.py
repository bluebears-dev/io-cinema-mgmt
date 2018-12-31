import os

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.serializers.movies import MovieSerializer, MovieDetailsSerializer
from .models import Cinema, TicketType, Showing, Movie
from .serializers import CinemaSerializer, TicketTypeSerializer, ShowingSerializer


class CinemaListView(APIView):
    def get(self, request, format=None):
        """
            Returns list of all cinemas in the system (with details)
        """
        cinema = Cinema.objects.all()
        serializer = CinemaSerializer(cinema, many=True)
        return Response(serializer.data)


class TicketTypeView(APIView):
    def get(self, request, format=None):
        """
            Returns list of all types of tickets in the system (with details)
        """
        ticket_type = TicketType.objects.all()
        serializer = TicketTypeSerializer(ticket_type, many=True)
        return Response(serializer.data)


class MoviesView(APIView):
    def get(self, request, cinema, date, format=None):
        """
            Returns list of all showings in given cinema during given day
        """
        showing = Showing.objects.prefetch_related().filter(room__cinema__id=cinema, date=date).distinct('movie').all()
        serializer = MovieSerializer(map(lambda v: v.movie, showing), many=True)
        return Response(serializer.data)


class MovieDetailsView(APIView):
    def get(self, request, id, format=None):
        """
            Returns details of the movie with given id
        """
        movie = Movie.objects.prefetch_related().filter(id=id).all()
        serializer = MovieDetailsSerializer(movie, many=True)
        return Response(serializer.data)


class ShowingView(APIView):
    def get(self, request, id, date, cinema, format=None):
        """
            Returns list of all showings for given movie id and given day
        """
        showing = Showing.objects.prefetch_related().filter(room__cinema__id=cinema, movie__id=id,
                                                            date=date).all().order_by('hour')
        serializer = ShowingSerializer(showing, many=True)
        return Response(serializer.data)


def index(request):
    if os.environ.get('PRODUCTION'):
        return render(request, 'static/index.html')
    else:
        return render(request, 'index.html')
