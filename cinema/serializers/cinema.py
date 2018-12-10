from rest_framework import serializers

from cinema.models import Cinema, Showing, Room


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


class ShowingSerializer(serializers.ModelSerializer):
    hour = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Showing
        fields = ('date', 'hour', 'movie', 'room', 'audio_type', 'picture_type')
        read_only_fields = fields

# class CinemaMovieSerializer(serializers.ModelSerializer):
#     movie = MovieSerializer(read_only=True)
#     # room = RoomSerializer(read_only=True)
#
#     class Meta:
#         model = Showing
#         fields = ('movie',)
#         read_only_fields = fields
