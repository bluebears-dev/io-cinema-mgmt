from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException, Movie,\
  File, BASE_DIR, check_adding_model_instance_with_wrong_fields, MovieGenre


class MovieTest(CinemaModelTest):

  def test_str_representation(self):
    self.assertEqual(self.movie_wizard.__str__(), "Harry Potter")
    self.assertEqual(self.anime.__str__(), "Anime")
