"""This file contains base class for tests
It sets up the example database so
you don't have to write creations

It also creates variables that are easy access to those records"""

from django.test import TestCase
from cinema.models.booking import TicketType, Ticket, Booking
from cinema.models.user import UserProfile, User
from cinema.models.cinema import Showing, Cinema, Room, Seat
from cinema.models.movies import Movie
from django.core.files import File
from app.settings import MEDIA_ROOT, os


class CinemaModelTest(TestCase):
  def setUp(self):

    try:
      # create cinemas
      Cinema.objects.create(name='Wiosna', city='Kraków', address='ul. Budryka 2', postal_code='32-300',
                            phone_number='880 591 332')
      Cinema.objects.create(name='Lato', city='Warszawa', address='ul. Marszałkowska 5', postal_code='34-001',
                            phone_number='880 591 333')

      self.cinema_wiosna = Cinema.objects.get(name='Wiosna', city='Kraków', address='ul. Budryka 2', postal_code='32-300',
                            phone_number='880 591 332')
      self.cinema_lato = Cinema.objects.get(name='Lato', city='Warszawa', address='ul. Marszałkowska 5',
                                         postal_code='34-001', phone_number='880 591 333')

      # create some rooms
      Room.objects.create(name='Kinder sponsored', cinema=self.cinema_wiosna)

      self.room_kinder = Room.objects.get(name='Kinder sponsored', cinema=self.cinema_wiosna)

      # create some seats
      Seat.objects.create(room=self.room_kinder, realRow='A', realColumn=2)
      Seat.objects.create(room=self.room_kinder, realRow='A', realColumn=3)

      self.seat_a2 = Seat.objects.get(room=self.room_kinder, realRow='A', realColumn=2)
      self.seat_a3 = Seat.objects.get(room=self.room_kinder, realRow='A', realColumn=3)

      # create some movie
      Movie.objects.create(title='Harry Potter', releaseDate='2017-02-12', length='123', producer='J. K. Rowling',
                           description='You\'re a wizard, Harry',
                           cover=File(open(MEDIA_ROOT + '/tests/bohemian.jpg', 'rb')))

      self.movie_wizard = Movie.objects.get(title='Harry Potter', releaseDate='2017-02-12', length='123',
                                       producer='J. K. Rowling', description='You\'re a wizard, Harry')

      # create a showing
      Showing.objects.create(date='2018-12-23', hour='12:54', room=self.room_kinder,
                             movie=self.movie_wizard, audio_type=Showing.ORIGINAL, picture_type=Showing.TWO_DIM)

      self.showing_wizard1 = Showing.objects.get(date='2018-12-23', hour='12:54', room=self.room_kinder,
                             movie=self.movie_wizard, audio_type=Showing.ORIGINAL, picture_type=Showing.TWO_DIM)

      # create ticket types
      TicketType.objects.create(ticketType='Ulgowy', price=12.59, description='Children below 18 years old and disabled')
      TicketType.objects.create(ticketType='Normalny', price=59.12, description='Everyone else')

      self.ticket_type_ulgowy = TicketType.objects.get(ticketType='Ulgowy', price=12.59,
                                                  description='Children below 18 years old and disabled')
      self.ticket_type_normalny = TicketType.objects.get(ticketType='Normalny', price=59.12, description='Everyone else')

      # create a user
      User.objects.create(username="elemelek", password='ulala')
      self.user_elemelek = User.objects.get(username="elemelek", password='ulala')

      UserProfile.objects.create(user=self.user_elemelek, phone_number='880 111 533')
      self.user_profile_elemelek = UserProfile.objects.get(user=self.user_elemelek, phone_number='880 111 533')

      # create a booking
      Booking.objects.create(user=self.user_elemelek, state=Booking.INITIATED, showing=self.showing_wizard1)
      self.booking_wizard1_elemelek = Booking.objects.get(user=self.user_elemelek, state=Booking.INITIATED,
                                                          showing=self.showing_wizard1)


      # create a ticket
      Ticket.objects.create(booking=self.booking_wizard1_elemelek, seat=self.seat_a2, ticketType=self.ticket_type_ulgowy)
      self.ticket_one = Ticket.objects.get(booking=self.booking_wizard1_elemelek, seat=self.seat_a2,
                                           ticketType=self.ticket_type_ulgowy)

    # in case something goes wrong in setUp() the covers of movies are not deleted
    except Exception as ee:
      try:
        self.movie_wizard.delete()
      finally:
        raise ee

  # ######################
  def tearDown(self):

    try:
      # delete cinemas (on cascade delete every room, seat, showing, booking and ticket)
      self.cinema_wiosna.delete()
      self.cinema_lato.delete()

      # delete movies
      self.movie_wizard.delete()

      # delete ticket types
      self.ticket_type_ulgowy.delete()
      self.ticket_type_normalny.delete()

      # delete user (on cascade user profile)
      self.user_elemelek.delete()

    except Exception as e:
      print('Something went wrong when cleaning the test database.\n'
            'Are you sure you haven\' called delete() method on any '
            'of the test class fields?\n'
            'But this means the tearDown() method was called so the tests passed')
