import secrets
from sched import scheduler
from threading import Thread

import coreapi
import coreschema
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, schema, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from app import settings
from cinema.models import Showing, Booking

booking_scheduler = scheduler()


def worker():
    while True:
        booking_scheduler.run()


task = Thread(target=worker)
task.start()


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
        booking_scheduler.enter(settings.BOOKING_CANCELLATION_TIMEOUT, 1, cancel_booking, kwargs={
            'request': None,
            'booking_id': booking.id,
            'token': booking.token
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
            description='Temporary authorization token'
        )
    )
]))
@permission_classes(())
@authentication_classes(())
def cancel_booking(request, booking_id, format=None):
    try:
        booking = Booking.objects.get(pk=booking_id)
        if not booking.finished and booking.token == request.data.get('token'):
            events = [event for event in booking_scheduler.queue if event.kwargs.get('booking_id') == booking_id]
            if len(events):
                booking_scheduler.cancel(events[0])
            booking.delete()
            return Response(data={'detail': "Booking canceled"})
        else:
            return Response(
                data={'detail': 'Unauthorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )
    except ObjectDoesNotExist:
        raise Http404
