from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cinema, TicketType, Showing
from .serializers import CinemaSerializer, TicketTypeSerializer, CinemaShowingSerializer


class CinemaListView(APIView):
    def get(self, request, format=None):
        """
            Return a list of all cinemas in the system (with details)
        """
        cinema = Cinema.objects.all()
        serializer = CinemaSerializer(cinema, many=True)
        return Response(serializer.data)


class TicketTypeView(APIView):
    def get(self, request, format=None):
        """
            Return a list of all types of tickets in the system (with details)
        """
        ticket_type = TicketType.objects.all()
        serializer = TicketTypeSerializer(ticket_type, many=True)
        return Response(serializer.data)


class ShowingView(APIView):
    def get(self, request, format=None):
        """
            Return a list of all showings in the system (with details)
        """
        showing = Showing.objects.prefetch_related().all()
        serializer = CinemaShowingSerializer(showing, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'index.html')
