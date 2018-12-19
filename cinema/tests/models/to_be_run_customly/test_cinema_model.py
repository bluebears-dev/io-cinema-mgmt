from cinema.tests.models.base_for_tests import CinemaModelTest

class MovieTest(CinemaModelTest):

  def test_str_representation(self):
    self.assertEqual(self.cinema_lato.__str__(), "Lato")
    self.assertEqual(self.showing_wizard1.__str__(), "Harry Potter (2018-12-23 12:54:00)")
