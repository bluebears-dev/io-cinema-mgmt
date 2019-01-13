import os
from datetime import datetime, timedelta

import coreapi
import coreschema
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from cinema.models import Room
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
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name='cinema_id',
                required=True,
                location='path',
                schema=coreschema.Integer(
                    description='Identifier of the cinema'
                )
            ),
            coreapi.Field(
                name='date',
                required=True,
                location='path',
                schema=coreschema.String(
                    description='Date in format YYYY-MM-DD'
                )
            )
        ]
    )

    def get(self, request, cinema_id, date, format=None):
        """
            Returns list of all movies showed in given cinema during given day
        """
        showing = Showing.objects.prefetch_related().filter(room__cinema__id=cinema_id, date=date).distinct(
            'movie').all()
        serializer = MovieSerializer(map(lambda v: v.movie, showing), many=True)
        return Response(serializer.data)


class MovieDetailsView(APIView):
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name='movie_id',
                required=True,
                location='path',
                schema=coreschema.Integer(
                    description='Identifier of the movie'
                )
            )
        ]
    )

    def get(self, request, movie_id, format=None):
        """
            Returns details of the movie with given id
        """
        movie = Movie.objects.prefetch_related().filter(id=movie_id).all()
        serializer = MovieDetailsSerializer(movie, many=True)
        return Response(serializer.data)


class ShowingView(APIView):
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name='showing_id',
                required=True,
                location='path',
                schema=coreschema.Integer(
                    description='Identifier of the showing'
                )
            ),
        ]
    )

    def get(self, request, showing_id):
        """
            Returns details about specific showing
        """
        try:
            showing = Showing.objects.get(pk=showing_id)
            if showing.date < datetime.today().date() or datetime.combine(datetime.today(),
                                                                          showing.hour) <= datetime.now() + timedelta(
                    minutes=15):
                raise Http404
            serializer = ShowingSerializer(showing)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise Http404


class ShowingListView(APIView):
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name='date',
                required=True,
                location='path',
                schema=coreschema.String(
                    description='Date in format YYYY-MM-DD'
                )
            ),
            coreapi.Field(
                name='cinema_id',
                required=True,
                location='path',
                schema=coreschema.Integer(
                    description='Identifier of the cinema'
                )
            ),
            coreapi.Field(
                name='movie_id',
                required=True,
                location='path',
                schema=coreschema.Integer(
                    description='Identifier of the movie'
                )
            ),
        ]
    )

    def get(self, request, movie_id, date, cinema_id, format=None):
        """
            Returns list of all showings for given movie id and given day
        """
        datetime_date = datetime.strptime(date, '%Y-%m-%d').date()
        if datetime_date < datetime.now().date():
            return Response([])
        elif datetime_date == datetime.now().date():
            showing = Showing.objects \
                .prefetch_related() \
                .filter(room__cinema__id=cinema_id,
                        movie__id=movie_id,
                        date=date,
                        hour__gt=datetime.now() + timedelta(minutes=15)) \
                .all() \
                .order_by('hour')
        else:
            showing = Showing.objects \
                .prefetch_related() \
                .filter(room__cinema__id=cinema_id,
                        movie__id=movie_id,
                        date=date) \
                .all() \
                .order_by('hour')
        serializer = ShowingSerializer(showing, many=True)
        return Response(serializer.data)


class RoomView(APIView):
    CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name='room_id',
                required=True,
                location='path',
                schema=coreschema.Integer(
                    description='Identifier of the room'
                )
            ),
        ]
    )

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
        for seat, column in zip(row, range(1, len(row) + 1)):
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

    def get(self, request, room_id):
        """
            Returns details of the room for given showing
        """
        try:
            room = Room.objects.get(pk=room_id)
            serializer = RoomSerializer(room)
            layout = self._transform_layout(serializer.data['rows'], serializer.data['layout'])
            data = serializer.data
            data['layout'] = layout
            return Response(data)
        except ObjectDoesNotExist:
            raise Http404


def index(request):
    if os.environ.get('PRODUCTION'):
        return render(request, 'static/index.html')
    else:
        return render(request, 'index.html')
