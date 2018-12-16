from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException, Movie,\
  File, BASE_DIR, check_adding_model_instance_with_wrong_fields


class MovieTest(CinemaModelTest):

  def test_str_representation(self):
    self.assertEqual(self.movie_wizard.__str__(), "Harry Potter")

  def test_adding_the_wrong_value(self):
    # add a movie
    Movie.objects.create(title='Black clover', releaseDate='2011-02-22', length=1200, producer="Przemysław Indyka",
                         description="5 leave clover and great mystery of the future",
                         cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie with a duplicate name
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='Black clover',
                                                  releaseDate='2011-02-22', length=1200, producer="Przemysław Indyka",
                                                  description="5 leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))
