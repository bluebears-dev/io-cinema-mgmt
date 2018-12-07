from cinema.models import Cinema, Showing, Room
from .movies import MovieSerializer
from rest_framework import serializers


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'city', 'address', 'postal_code', 'phone_number')
        read_only_fields = fields


class RoomSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'name', 'cinema')
        read_only_fields = fields


class CinemaShowingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Showing
        fields = ('id', 'date', 'room', 'movie', 'audio_type', 'picture_type')
        read_only_fields = fields
