from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException, TicketType
from cinema.tests.models.base_for_tests import Booking, Ticket



class BookingTest(CinemaModelTest):

  def test_str_representation(self):

    self.assertEqual(self.ticket_type_ulgowy.__str__(), "Ulgowy")
    self.assertEqual(self.ticket_type_normalny.__str__(), "Normalny")

    self.assertEqual(self.booking_wizard1_elemelek.__str__(), "Rezerwacja na Seans 2018-12-23 12:54:00 : Harry Potter")

    self.assertEqual(self.ticket_one.__str__(), "Bilet na Rezerwacja na Seans 2018-12-23 12:54:00 : Harry Potter")

  def test_adding_of_wrong_values_of_ticket_type(self):

    ###
    try:
      TicketType.objects.create(ticketType='Ulgowy', price=121.43, description="random letters")

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating ticket type with duplicate name")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

    ###
    try:
      TicketType.objects.create(ticketType='TwoRandom', price=111111121.43, description="random letters")

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating ticket type with too long price")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

    ###
    try:
      TicketType.objects.create(ticketType=None, price=121.433, description="random letters")

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating ticket type with None ticketType")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

      ###
      try:
        TicketType.objects.create(ticketType='FourRandom', price=None, description="random letters")

        raise NoTestOccuredException()
      except NoTestOccuredException as e:
        print("Exception should occur but it hadn't when creating ticket type with None price")
        raise e
      except Exception as e:
        print("Info: " + e.__str__())
        pass

  def test_adding_wrong_value_of_booking(self):

    ###
    try:
      Booking.objects.create(user=None, showing=self.showing_wizard1, state=Booking.INITIATED)

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating booking with None user")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

    ###
    try:
      Booking.objects.create(user=self.user_elemelek, showing=None, state=Booking.INITIATED)

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating booking with None showing")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

    ###
    try:
      Booking.objects.create(user=self.user_elemelek, showing=self.showing_wizard1, state=Booking.CHOICES_FOR_STATE)

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating booking with state of different type")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

    ###
    try:
      Booking.objects.create(user=None, showing=self.showing_wizard1, state='ULALA')

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating booking with None user second attempt")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

  def test_adding_wrong_value_of_ticket(self):

    try:
      Ticket.objects.create(booking=None, seat=self.seat_a2, ticketType=self.ticket_type_normalny)

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating ticket with None booking")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

    try:
      Ticket.objects.create(booking=self.booking_wizard1_elemelek, seat=None,
                            ticketType=self.ticket_type_normalny)

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating ticket with None seat")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

    try:
      Ticket.objects.create(booking=None, seat=self.seat_a2, ticketType=None)

      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating ticket with None ticket type")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass

