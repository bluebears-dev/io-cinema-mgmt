from cinema.tests.models.base_for_tests import check_adding_model_instance_with_wrong_fields
from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException, TicketType


class BookingTest(CinemaModelTest):
    def test_str_representation(self):

        self.assertEqual(self.ticket_type_ulgowy.__str__(), "Ulgowy")
        self.assertEqual(self.ticket_type_normalny.__str__(), "Normalny")

    def test_adding_of_wrong_values_of_ticket_type(self):

        # try to add a ticket type that already exists
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with duplicate name",
                                                      name="Ulgowy", price=121.43, description="random letters")

        # try to add ticket type with too long price
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with too long price",
                                                      name='TwoRandom', price=111111121.43,
                                                      description="random letters")

        # try to add ticket type with no name
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with None ticketType", name=None,
                                                      price=121.433, description="random letters")

        # try to add ticket type with no price
        check_adding_model_instance_with_wrong_fields(TicketType, "Exception should occur but it hadn't when creating "
                                                                  "ticket type with None price",
                                                      name='FourRandom', price=None, description="random letters")
