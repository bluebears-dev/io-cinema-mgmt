from rest_framework import serializers

from cinema.models import Cinema, Room


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
