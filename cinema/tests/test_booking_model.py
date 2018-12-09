from cinema.tests.testbase import CinemaModelTest, TicketType



class BookingTest(CinemaModelTest):

  def test_str_representation(self):

    self.assertEqual(self.ticket_type_ulgowy.__str__(), "Ulgowy")
    self.assertEqual(self.ticket_type_normalny.__str__(), "Normalny")

    # self.assertEqual(self.booking_wizard1_elemelek.__str__(), "Rezerwacja na ")
