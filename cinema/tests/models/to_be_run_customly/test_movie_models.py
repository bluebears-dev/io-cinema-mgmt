from cinema.tests.models.base_for_tests import CinemaModelTest, NoTestOccuredException, Movie, File, MEDIA_ROOT


class MovieTest(CinemaModelTest):

  def test_str_representation(self):
    self.assertEqual(self.movie_wizard.__str__(), "Harry Potter")

  def test_adding_the_wrong_value(self):

    ###
    try:
      Movie.objects.create(title='Black clover', releaseDate='2011-02-22', length=1200, producer="Przemysław Indyka",
                           description="5 leave clover and great mystery of the future",
                           cover=File(open(MEDIA_ROOT + '/tests/bohemian.jpg', 'rb')))

      Movie.objects.create(title='Black clover', releaseDate='2011-02-22', length=1200, producer="Przemysław Indyka",
                           description="5 leave clover and great mystery of the future",
                           cover=File(open(MEDIA_ROOT + '/tests/bohemian.jpg', 'rb')))


      raise NoTestOccuredException()
    except NoTestOccuredException as e:
      print("Exception should occur but it hadn't when creating ticket type with duplicate name")
      raise e
    except Exception as e:
      print("Info: " + e.__str__())
      pass
