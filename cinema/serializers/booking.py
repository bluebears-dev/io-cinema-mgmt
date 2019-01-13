from rest_framework import serializers

from cinema.models import TicketType, Booking


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ('id', 'ticketType', 'price', 'description')
        read_only_fields = fields


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'showing')
