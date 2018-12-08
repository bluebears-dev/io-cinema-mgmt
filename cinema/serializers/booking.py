from cinema.models import TicketType
from rest_framework import serializers


class TicketTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = TicketType
		fields = ('id', 'ticketType', 'price', 'description')
		read_only_fields = fields