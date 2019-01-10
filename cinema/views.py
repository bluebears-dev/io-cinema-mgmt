import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.serializers import RoomSerializer
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


class RoomView(APIView):
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @staticmethod
    def _map_number_to_char(number):
        if number - 1 >= len(RoomView.CHARS):
            return None
        else:
            return RoomView.CHARS[number - 1]

    @staticmethod
    def _transform_row(row):
        previous_seat = [0, 0]
        result = []
        for seat, column in zip(row, range(1, len(row))):
            result += [None for _ in range(seat[1] - previous_seat[1] - 1)]
            result.append({'col': column, 'seat': seat})
            previous_seat = seat
        return result

    @staticmethod
    def _transform_layout(rows, raw_layout):
        layout = []
        empty = 0
        for current_row in range(1, rows + 1):
            row = [i for i in raw_layout if i[0] == current_row]
            if len(row):
                layout.append({
                    'row': RoomView._map_number_to_char(current_row - empty),
                    'seats': RoomView._transform_row(row)
                })
            else:
                layout.append(None)
                empty += 1
        return layout

    def get(self, request, showing_id):
        showing = Showing.objects.filter(id=showing_id)
        if len(showing) == 1:
            room = showing[0].room
            serializer = RoomSerializer(room)
            layout = self._transform_layout(serializer.data['rows'], serializer.data['layout'])
            data = serializer.data
            data['layout'] = layout
            return Response(data)
        else:
            return HttpResponse(status=404)


def index(request):
    if os.environ.get('PRODUCTION'):
        return render(request, 'static/index.html')
    else:
        return render(request, 'index.html')
