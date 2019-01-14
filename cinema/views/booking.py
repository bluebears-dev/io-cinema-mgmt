import secrets
from sched import scheduler
from threading import Thread

import coreapi
import coreschema
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, schema, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from app import settings
from cinema.models import Showing, Booking, Ticket
from cinema.serializers.booking import TicketSerializer

booking_scheduler = scheduler()


def worker():
    while True:
        booking_scheduler.run()


task = Thread(target=worker)
task.start()


def cancel(booking_id):
    booking = Booking.objects.get(pk=booking_id)
    booking.delete()
    print("Canceled: {}".format(booking_id))


def check_booking_token(booking_instance, token):
    if booking_instance.finished and booking_instance.token != token:
        raise PermissionError


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field(
        name='showing_id',
        required=True,
        location='path',
        schema=coreschema.Integer(
            description='Identifier of the showing'
        )
    )
]))
@permission_classes(())
@authentication_classes(())
def book_showing(request, showing_id, format=None):
    """
        Creates new booking
    """
    try:
        showing = Showing.objects.get(pk=showing_id)
        booking = Booking.objects.create(showing=showing, token=secrets.token_urlsafe(64))
        booking_scheduler.enter(settings.BOOKING_CANCELLATION_TIMEOUT, 1, cancel, kwargs={
            'booking_id': booking.id,
        })
        return Response(
            data={
                'id': booking.id,
                'token': booking.token
            },
            status=status.HTTP_201_CREATED
        )
    except ObjectDoesNotExist:
        return Response(
            data={'detail': 'Showing of requested id has not been found'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['DELETE'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field(
        name='booking_id',
        required=True,
        location='path',
        schema=coreschema.Integer(
            description='Identifier of the booking'
        )
    ),
    coreapi.Field(
        name='token',
        required=True,
        location='form',
        schema=coreschema.String(
            description='Temporary authorization token assigned during booking'
        )
    )
]))
@permission_classes(())
@authentication_classes(())
def cancel_booking(request, booking_id, format=None):
    try:
        booking = Booking.objects.get(pk=booking_id)
        check_booking_token(booking, request.data.get('token'))
        events = [event for event in booking_scheduler.queue if event.kwargs.get('booking_id') == booking_id]
        if len(events):
            booking_scheduler.cancel(events[0])
        booking.delete()
        return Response(data={'detail': "Booking canceled"})
    except PermissionError:
        return Response(
            data={'detail': 'Unauthorized'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except ObjectDoesNotExist:
        raise Http404


@api_view(['PUT'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field(
        name='booking_id',
        required=True,
        location='path',
        schema=coreschema.Integer(
            description='Identifier of the booking'
        )
    ),
    coreapi.Field(
        name='token',
        required=True,
        location='form',
        schema=coreschema.String(
            description='Temporary authorization token assigned during booking'
        )
    ),
    coreapi.Field(
        name='tickets',
        required=True,
        location='form',
        schema=coreschema.Array(
            description='Array with ticket data\'s',
        )
    )
]))
@permission_classes(())
@authentication_classes(())
def replace_tickets(request, booking_id, format=None):
    """
        Removes old and creates new tickets for specified booking
    """
    try:
        booking = Booking.objects.get(pk=booking_id)
        check_booking_token(booking, request.data.get('token'))
        tickets = request.data.get('tickets', [])
        for ticket in tickets:
            ticket['booking'] = booking_id
        print(tickets)
        serializer = TicketSerializer(data=tickets, many=True)
        with transaction.atomic():
            for ticket in Ticket.objects.filter(booking=booking_id).all():
                ticket.delete()
            if serializer.is_valid():
                serializer.save()
                return Response(data={'detail': 'Tickets replaced'})
            else:
                return Response(
                    data={'detail': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
    except ValidationError as e:
        return Response(
            data={'detail': e},
            status=status.HTTP_400_BAD_REQUEST)
    except PermissionError:
        return Response(
            data={'detail': 'Unauthorized'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except ObjectDoesNotExist:
        return Response(
            data={'detail': 'Booking of requested id has not been found'},
            status=status.HTTP_404_NOT_FOUND
        )
