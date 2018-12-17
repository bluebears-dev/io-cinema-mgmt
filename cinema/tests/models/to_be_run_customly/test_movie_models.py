from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException, Movie,\
  File, BASE_DIR, check_adding_model_instance_with_wrong_fields, MovieGenre


class MovieTest(CinemaModelTest):

  def test_str_representation(self):
    self.assertEqual(self.movie_wizard.__str__(), "Harry Potter")
    self.assertEqual(self.anime.__str__(), "Anime")

  def test_adding_the_wrong_value(self):
    # add a movie
    Movie.objects.create(title='Black clover', releaseDate='2011-02-22', length=1200, producer="Przemysław Indyka",
                         description="5 leave clover and great mystery of the future",
                         cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie with a duplicate name
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating movie "
                                                         "with duplicate name", title='Black clover',
                                                  releaseDate='2011-02-22', length=1200, producer="Przemysław Indyka",
                                                  description="5 leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a name
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating movie "
                                                         "without a name", title=None,
                                                  releaseDate='2011-02-23', length=120, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a release date
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating movie "
                                                         "without release date", title='elomelo',
                                                  releaseDate=None, length=120, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # future dates should be possible, let's assume that the release is to take place in our cinema
    Movie.objects.create(title='Back to the Futura', releaseDate='2091-02-22', length=1200,
                         producer="Przemysław Indyka",
                         description="5 leave clover and great mystery of the future",
                         cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a length
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating movie "
                                                         "without a length", title='ulamulamulam',
                                                  releaseDate='2011-02-23', length=None, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a producer
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating movie "
                                                         "without a producer", title='dondorere',
                                                  releaseDate='2011-02-23', length=123, producer=None,
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a description
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating movie "
                                                         "without a description", title='dondorere',
                                                  releaseDate='2011-02-23', length=123, producer="elemelek",
                                                  description=None,
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

  def test_movie_genre(self):
    # try to add a movie genre without a name
    check_adding_model_instance_with_wrong_fields(MovieGenre, "Exception should have occured but it hadn't when"
                                                              " creating movie genre without a name", name=None)
    # try to add a movie genre with too long name
    check_adding_model_instance_with_wrong_fields(MovieGenre, "Exception should have occured but it hadn't when"
                                                              " creating movie genre with too long name",
                                                  name="paraliz"*20)
