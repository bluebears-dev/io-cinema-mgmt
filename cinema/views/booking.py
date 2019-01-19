import json
import os
import secrets
import time
from io import BytesIO
from sched import scheduler

import coreapi
import coreschema
import pdfkit
import qrcode
import qrcode.image.svg
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.files.base import ContentFile
from django.db import transaction
from django.http import Http404
from django.template.loader import get_template
from rest_framework import status
from rest_framework.decorators import api_view, schema, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from app import settings
from cinema.models import Showing, Booking, Ticket
from cinema.serializers.booking import TicketSerializer
from cinema.serializers.user import ClientSerializer
from .cinema import RoomView

booking_scheduler = scheduler()


def worker():
    while True:
        booking_scheduler.run()


def cancel(booking_id):
    booking = Booking.objects.get(pk=booking_id)
    booking.delete()
    print("Canceled: {}".format(booking_id))


def check_booking_token(booking_instance, token):
    if booking_instance.finished or booking_instance.token != token:
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
        location='query',
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
        check_booking_token(booking, request.query_params.get('token'))
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
        serializer = TicketSerializer(data=tickets, many=True)
        with transaction.atomic():
            for ticket in Ticket.objects.filter(booking=booking_id).all():
                ticket.delete()
            if serializer.is_valid():
                serializer.save()
                tickets = Ticket.objects.prefetch_related().filter(booking=booking_id).all()
                total_price = sum([ticket.ticket_type.price for ticket in tickets if ticket.ticket_type])
                booking.total_cost = total_price
                booking.save()
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
        name='client_data',
        required=True,
        location='form',
        schema=coreschema.Object(
            description='Client data like first name, last name, email and phone number',
        )
    )
]))
@permission_classes(())
@authentication_classes(())
def replace_client_data(request, booking_id, format=None):
    """
        Removes old and creates new client information instance
    """
    try:
        booking = Booking.objects.get(pk=booking_id)
        check_booking_token(booking, request.data.get('token'))
        client_data = request.data.get('client_data', {})
        client_data['username'] = secrets.token_urlsafe(10)
        serializer = ClientSerializer(data=client_data)
        with transaction.atomic():
            if booking.user:
                booking.user.delete()
            if serializer.is_valid():
                booking.user = serializer.save()
                booking.save()
                return Response(data={'detail': 'Client data replaced'})
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


@api_view(['POST'])
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
def booking_timeout_webhook(request, booking_id, format=None):
    """
        Returns error if booking has been canceled or returns normally when its finished
    """
    try:
        booking = Booking.objects.get(pk=booking_id)
        check_booking_token(booking, request.data.get('token'))
        while not booking.finished:
            time.sleep(60)
            booking = Booking.objects.get(pk=booking_id)
        return Response(data={'detail': 'Booking finished'})
    except PermissionError:
        return Response(
            data={'detail': 'Unauthorized'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except ObjectDoesNotExist:
        return Response(
            data={'detail': 'Booking not found or canceled'},
            status=status.HTTP_404_NOT_FOUND
        )


def generate_pdf(booking_instance):
    tickets = Ticket.objects.filter(booking=booking_instance.id).all()
    seats = []

    room = booking_instance.showing.room
    labeled_layout = RoomView._transform_layout(room.rows, room.layout)
    labeled_layout = [x for x in labeled_layout if x]

    for ticket in tickets:
        is_next = False
        for row in labeled_layout:
            for seat in row['seats']:
                if seat and (seat['seat'][0], seat['seat'][1]) == (ticket.row, ticket.column):
                    seats.append('{}{}'.format(row['row'], seat['col']))
                    is_next = True
                    break
            if is_next:
                break

    ticket_types = [ticket.ticket_type.name for ticket in tickets]
    ticket_type_labels = ['{}x {}'.format(ticket_types.count(ticket_type), ticket_type) for ticket_type in
                          set(ticket_types)]
    template = get_template(os.path.join(settings.BASE_DIR, 'cinema', 'ticket', 'template.html'))

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
        image_factory=qrcode.image.svg.SvgPathImage
    )
    qr.add_data(json.dumps({
        'booking_id': booking_instance.id,
        'token': booking_instance.token,
        'cinema': booking_instance.showing.room.cinema.name,
        'room': booking_instance.showing.room.name,
        'movie': booking_instance.showing.movie.title,
        'date': '{}, {}'.format(booking_instance.showing.date, booking_instance.showing.hour),
        'seats': ', '.join(seats),
        'ticket_types': ticket_type_labels,
    }))
    qr.make()
    image_qr = qr.make_image()
    buffer = BytesIO()
    image_qr.save(buffer)

    html = template.render({
        'cinema': booking_instance.showing.room.cinema.name,
        'room': booking_instance.showing.room.name,
        'movie': booking_instance.showing.movie.title,
        'date': '{}, {}'.format(booking_instance.showing.date, booking_instance.showing.hour),
        'seats': ', '.join(seats),
        'ticket_types': ticket_type_labels,
        'qr': str(buffer.getvalue().split(b'\n')[1], 'utf-8')
    })
    file = pdfkit.from_string(html, False)
    booking_instance.pdf_file.save('out.pdf', ContentFile(file))


@api_view(['POST'])
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
def finalize_booking(request, booking_id, format=None):
    """
        Finish booking or return error, if some data is missing
    """
    try:
        booking = Booking.objects.get(pk=booking_id)
        check_booking_token(booking, request.data.get('token'))
        if not booking.user or not booking.total_cost > 0:
            raise AssertionError
        events = [event for event in booking_scheduler.queue if event.kwargs.get('booking_id') == booking_id]
        if len(events):
            booking_scheduler.cancel(events[0])
        booking.finished = True
        booking.state = Booking.UNPAID
        generate_pdf(booking)
        booking.save()
        return Response(data={'detail': 'Finished'})
    except AssertionError:
        return Response(
            data={'detail': 'Not finished'},
            status=status.HTTP_400_BAD_REQUEST
        )
    except PermissionError:
        return Response(
            data={'detail': 'Unauthorized'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    except ObjectDoesNotExist:
        return Response(
            data={'detail': 'Booking not found or canceled'},
            status=status.HTTP_404_NOT_FOUND
        )
