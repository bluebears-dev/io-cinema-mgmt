import coreapi
import coreschema
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from cinema.models import TicketType, Showing, Movie
from cinema.serializers import TicketTypeSerializer
from cinema.serializers.movies import MovieSerializer, MovieDetailsSerializer


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
