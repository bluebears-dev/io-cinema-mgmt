import os

from django.shortcuts import render

from .booking import book_showing, cancel_booking, replace_tickets, replace_client_data, booking_timeout_webhook, \
    finalize_booking
from .cinema import CinemaListView, RoomView, ShowingListView, ShowingView, get_booked_seats
from .movies import MovieDetailsView, MoviesView, TicketTypeView
from .payment import get_payu_oauth_token, get_pay_methods, create_order, get_order_details


def index(request):
    if os.environ.get('PRODUCTION'):
        return render(request, 'static/index.html')
    else:
        return render(request, 'index.html')
