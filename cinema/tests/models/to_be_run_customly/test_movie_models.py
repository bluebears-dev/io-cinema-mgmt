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

    # try to add a movie without a name
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title=None,
                                                  releaseDate='2011-02-23', length=120, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a release date
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='elomelo',
                                                  releaseDate=None, length=120, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # future dates should be possible, let's assume that the release is to take place in our cinema
    Movie.objects.create(title='Back to the Futura', releaseDate='2091-02-22', length=1200,
                         producer="Przemysław Indyka",
                         description="5 leave clover and great mystery of the future",
                         cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie with pessimistic length
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='elomelo',
                                                  releaseDate=None, length=-120, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie with zero length
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='elomelo',
                                                  releaseDate=None, length=0, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a length
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='ulamulamulam',
                                                  releaseDate='2011-02-23', length=None, producer="Przemysław Indyka",
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie without a producer
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='dondorere',
                                                  releaseDate='2011-02-23', length=123, producer=None,
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie with empty producer
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='dondorere',
                                                  releaseDate='2011-02-23', length=123, producer='',
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

    # try to add a movie with empty title
    check_adding_model_instance_with_wrong_fields(Movie, "Exception should occur but it hadn't when creating ticket "
                                                         "type with duplicate name", title='',
                                                  releaseDate='2011-02-23', length=123, producer='Przemko',
                                                  description="fajf leave clover and great mystery of the future",
                                                  cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))
