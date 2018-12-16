from cinema.tests.models.base_for_tests import Booking, Ticket, check_adding_model_instance_with_wrong_fields
from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException, TicketType


class BookingTest(CinemaModelTest):
    def test_str_representation(self):

        self.assertEqual(self.ticket_type_ulgowy.__str__(), "Ulgowy")
        self.assertEqual(self.ticket_type_normalny.__str__(), "Normalny")

        self.assertEqual(self.booking_wizard1_elemelek.__str__(),
                         "Rezerwacja na Harry Potter (2018-12-23 12:54:00)")

        self.assertEqual(self.ticket_one.__str__(), "Bilet na Rezerwacja na Harry Potter (2018-12-23 12:54:00)")

    def test_adding_of_wrong_values_of_ticket_type(self):

        # try to add a ticket type that already exists
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with duplicate name",
                                                      ticketType='Ulgowy', price=121.43, description="random letters")

        # try to add ticket type with too long price
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with too long price",
                                                      ticketType='TwoRandom', price=111111121.43,
                                                      description="random letters")

        # try to add ticket type with no name
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with None ticketType", ticketType=None,
                                                      price=121.433, description="random letters")

        # try to add ticket type with no price
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with None price",
                                                      ticketType='FourRandom', price=None, description="random letters")

    def test_adding_wrong_value_of_booking(self):

        # try to add booking without the user
        check_adding_model_instance_with_wrong_fields(Booking, "Exception should occur but it hadn't when creating "
                                                               "booking with None user", user=None,
                                                      showing=self.showing_wizard1, state=Booking.INITIATED)

        # try to add booking without a showing
        check_adding_model_instance_with_wrong_fields(Booking, "Exception should occur but it hadn't when creating "
                                                               "booking with None showing", user=self.user_elemelek,
                                                      showing=None, state=Booking.INITIATED)

        # try to add booking with state taken out of nowhere
        check_adding_model_instance_with_wrong_fields(Booking, "Exception should occur but it hadn't when creating "
                                                               "booking with state of different type",
                                                      user=self.user_elemelek, showing=self.showing_wizard1,
                                                      state=Booking.CHOICES_FOR_STATE)

        check_adding_model_instance_with_wrong_fields(Booking, "Exception should occur but it hadn't when creating "
                                                               "booking with state of different type",
                                                      user=self.user_elemelek, showing=self.showing_wizard1,
                                                      state="Something random")

    def test_adding_wrong_value_of_ticket(self):

        # try to add a ticket with no booking
        check_adding_model_instance_with_wrong_fields(Ticket, "Exception should occur but it hadn't when creating "
                                                              "ticket with no booking", booking=None,
                                                      seat=self.seat_a2, ticketType=self.ticket_type_normalny)

        # try to add a ticket with no seat
        check_adding_model_instance_with_wrong_fields(Ticket, "Exception should occur but it hadn't when creating "
                                                              "ticket with no seat",
                                                      booking=self.booking_wizard1_elemelek, seat=None,
                                                      ticketType=self.ticket_type_normalny)

        # try to add a ticket without ticket type
        check_adding_model_instance_with_wrong_fields(Ticket, "Exception should occur but it hadn't when creating "
                                                              "ticket with no ticket type",
                                                      booking=self.booking_wizard1_elemelek,
                                                      seat=self.seat_a2, ticketType=None)
