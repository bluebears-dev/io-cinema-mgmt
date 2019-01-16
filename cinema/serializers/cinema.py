from rest_framework import serializers

from cinema.models import Cinema, Showing, Room, Ticket


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id', 'name', 'city', 'address', 'postal_code', 'phone_number')
        read_only_fields = fields


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'cinema', 'rows', 'cols', 'layout')
        read_only_fields = fields


class ShowingSerializer(serializers.ModelSerializer):
    hour = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Showing
        fields = ('id', 'date', 'hour', 'movie', 'room', 'audio_type', 'picture_type')
        read_only_fields = fields


class BookedSeatsSerializer(serializers.ModelSerializer):
    seat = serializers.SerializerMethodField('get_seats')

    class Meta:
        model = Ticket
        fields = ('seat',)

    def get_seats(self, obj):
        """

        :param obj:
        :return: list containing coordinates of booked seat
        """
        return [obj.row, obj.column]
