import os
import time

import coreapi
import coreschema
import requests
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, schema, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from cinema.models import Booking
from cinema.serializers.booking import BookingSerializer


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field(
        name='client_id',
        required=True,
        location='form',
        schema=coreschema.String(
            description='POS client id'
        )
    ),
    coreapi.Field(
        name='client_secret',
        required=True,
        location='form',
        schema=coreschema.String(
            description='POS client secret'
        )
    )
]))
@permission_classes(())
@authentication_classes(())
def get_payu_oauth_token(request, format=None):
    """
        Proxy for PayU OAuth token retrieval.
        Returns OAuth token
    """
    data = requests.post(
        'https://secure.snd.payu.com/pl/standard/user/oauth/authorize',
        data={
            'grant_type': 'client_credentials',
            'client_id': request.data.get('client_id'),
            'client_secret': request.data.get('client_secret')
        }
    )
    return Response(data=data.json())


@api_view(['GET'])
@permission_classes(())
@authentication_classes(())
def get_pay_methods(request, format=None):
    """
        Proxy for pay methods fetching.
        Requires X-AUTHORIZATION header for OAuth.
    """
    headers = {
        'Authorization': request.META.get('HTTP_X_AUTHORIZATION'),
        'Content-Type': "application/json",
    }

    data = requests.get('https://secure.snd.payu.com/api/v2_1/paymethods/', headers=headers)
    return Response(data=data.json(), status=data.status_code)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field(
        name='booking_id',
        required=True,
        location='path',
        schema=coreschema.String(
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
        name='method',
        required=True,
        location='form',
        schema=coreschema.String(
            description='Payment method'
        )
    )
]))
@permission_classes(())
@authentication_classes(())
def create_order(request, booking_id, format=None):
    """
        Proxy for order creation.
        Requires X-AUTHORIZATION header for OAuth.
    """
    headers = {
        'Authorization': request.META.get('HTTP_X_AUTHORIZATION'),
        'Content-Type': "application/json",
    }
    try:
        booking = Booking.objects.get(pk=booking_id)
        if booking.token != request.data.get('token'):
            raise PermissionError
        payu_data = {
            'continueUrl': 'http://{}/#/bilet/{}/{}'.format(os.environ.get('HOST'), booking.id, booking.token),
            'customerIp': os.environ.get('HOST'),
            'merchantPosId': '348348',
            'description': 'Kinio KAPPA',
            'currencyCode': 'PLN',
            'totalAmount': str(int(booking.total_cost * 100)),
            'buyer': {
                'email': booking.user.email,
                'firstName': booking.user.first_name,
                'lastName': booking.user.last_name,
                'phone': '+48' + booking.user.client_profile.phone_number
            },
            'products': [
                {
                    'name': 'Bilety na {}'.format(booking.showing.movie.title),
                    'unitPrice': str(int(booking.total_cost * 100)),
                    'quantity': '1'
                }
            ],
            'payMethods': {
                'payMethod': {
                    'type': 'PBL',
                    'value': request.data.get('method')
                }
            }
        }
        data = requests.post(
            'https://secure.snd.payu.com/api/v2_1/orders',
            json=payu_data,
            headers=headers,
            allow_redirects=False
        )
        json_data = data.json()
        booking.transaction_id = json_data.get('orderId', None)
        booking.save()
        status_code = data.status_code if data.status_code != 301 and data.status_code != 302 else 200
        return Response(data=json_data, status=status_code)
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


@api_view(['GET'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field(
        name='booking_id',
        required=True,
        location='path',
        schema=coreschema.String(
            description='Identifier of the booking'
        )
    ),
    coreapi.Field(
        name='token',
        required=True,
        location='path',
        schema=coreschema.String(
            description='Temporary authorization token assigned during booking'
        )
    ),
]))
@permission_classes(())
@authentication_classes(())
def get_order_details(request, booking_id, token, format=None):
    """
        Proxy request to PayU order information. Returns information about booking and sets status.
        Requires passing X-Authorization header with OAuth token for PayU.
    """
    try:
        headers = {
            'Authorization': request.META.get('HTTP_X_AUTHORIZATION'),
            'Content-Type': "application/json",
        }

        booking = Booking.objects.get(pk=booking_id)
        if booking.token != token:
            raise PermissionError
        time.sleep(2)
        data = requests.get(
            'https://secure.snd.payu.com/api/v2_1/orders/{}'.format(booking.transaction_id),
            headers=headers
        )
        json_data = data.json()
        order_status = json_data['orders'][0]['status']
        if order_status == 'CANCELED':
            booking.delete()
            return Response()
        elif order_status == 'COMPLETED':
            booking.state = Booking.PAID
            booking.save()
        serializer = BookingSerializer(booking)
        return Response(data=serializer.data)
    except ObjectDoesNotExist or PermissionError:
        return Response(
            data={'detail': 'Booking not found or canceled'},
            status=status.HTTP_404_NOT_FOUND
        )
