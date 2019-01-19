from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException,\
  check_adding_model_instance_with_wrong_fields
from cinema.models.cinema import *

class MovieTest(CinemaModelTest):

  def test_str_representation(self):
    self.assertEqual(self.cinema_lato.__str__(), "Lato")
    self.assertEqual(self.showing_wizard1.__str__(), "Harry Potter (2018-12-23 12:54:00)")
    self.assertEqual(self.room_kinder.__str__(), "Kinder (Wiosna)")

  def test_adding_wrong_values(self):
    check_adding_model_instance_with_wrong_fields(Cinema, "No exception occurred when creating cinema with duplicate"
                                                          "name", name="Lato", city='Kraków',
                                                  address='ul. Budryka 7', postal_code='32-300',
                                                  phone_number='880 231 332')

    check_adding_model_instance_with_wrong_fields(Cinema, "No exception occurred despite wrong postal code when"
                                                          "creating a cinema", name="Buziak", city='Wrocław',
                                                  address='ul. Gombrowicza 7', postal_code='52-3077',
                                                  phone_number='888 231 332')

