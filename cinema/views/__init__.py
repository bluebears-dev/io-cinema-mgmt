import os

from django.shortcuts import render

from .booking import book_showing, cancel_booking, replace_tickets
from .cinema import CinemaListView, RoomView, ShowingListView, ShowingView, get_booked_seats
from .movies import MovieDetailsView, MoviesView, TicketTypeView


def index(request):
    if os.environ.get('PRODUCTION'):
        return render(request, 'static/index.html')
    else:
        return render(request, 'index.html')
