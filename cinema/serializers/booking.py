from django.db import transaction
from rest_framework import serializers

from cinema.models import TicketType, Booking, Ticket


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ('id', 'ticketType', 'price', 'description')
        read_only_fields = fields


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'showing')


class TicketListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        tickets = []
        with transaction.atomic():
            for ticket in validated_data:
                tickets.append(self.child.create(ticket))
        print(tickets)
        return tickets


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        list_serializer_class = TicketListSerializer
        fields = ('booking', 'row', 'column', 'ticket_type')

    def create(self, validated_data):
        print(validated_data)
        ticket = Ticket.objects.create(**validated_data)
        return ticket

    def update(self, instance, validated_data):
        instance.ticket_type = validated_data.pop('ticket_type', instance.ticket_type)
        instance.row = validated_data.get('row', instance.row)
        instance.column = validated_data.get('column', instance.column)
        instance.save()

        return instance
