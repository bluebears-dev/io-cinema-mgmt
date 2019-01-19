"""This file contains base class for tests
It sets up the example database so
you don't have to write creations

It also creates variables that are easy access to those records

If OperationalError occurs when trying to run tests, try
python manage.py makemigrations
python manage.py migrate

Then tests should come back to normal"""

from django.core.files import File
from django.test import TransactionTestCase

from app.settings import BASE_DIR, MEDIA_ROOT, os
from cinema.models.booking import TicketType
from cinema.models.cinema import Showing, Cinema, Room
from cinema.models.movies import Movie, MovieGenre
from cinema.models.user import ClientProfile, User, EmployeeProfile


class CinemaModelTest(TransactionTestCase):
  def setUp(self):

    if os.listdir(MEDIA_ROOT + "/covers"):
      self.__been_there_before = os.listdir(MEDIA_ROOT + "/covers")
    else:
      self.__been_there_before = []

    if os.listdir(MEDIA_ROOT + "/thumbs"):
      self.__thumb_there_before = os.listdir(MEDIA_ROOT + "/thumbs")
    else:
      self.__thumb_there_before = []

    try:
      # create movie genres
      MovieGenre.objects.create(name="Horror")
      MovieGenre.objects.create(name="Anime")
      self.horro = MovieGenre.objects.get(name="Horror")
      self.horro.save()
      self.anime = MovieGenre.objects.get(name="Anime")
      self.anime.save()

      # create cinemas
      Cinema.objects.create(name='Wiosna', city='Kraków', address='ul. Budryka 2', postal_code='32-300',
                            phone_number='880 591 332')
      Cinema.objects.create(name='Lato', city='Warszawa', address='ul. Marszałkowska 5', postal_code='34-001',
                            phone_number='880 591 333')

      self.cinema_wiosna = Cinema.objects.get(name='Wiosna', city='Kraków', address='ul. Budryka 2', postal_code='32-300',
                            phone_number='880 591 332')
      self.cinema_lato = Cinema.objects.get(name='Lato', city='Warszawa', address='ul. Marszałkowska 5',
                                         postal_code='34-001', phone_number='880 591 333')

      # create some rooms
      Room.objects.create(name='Kinder', cinema=self.cinema_wiosna, rows=3, cols=3, json_layout="[[1, 1], [1, 2], [1, 3],"
                                                                                                " [2, 1], [2, 2], [2, 3],"
                                                                                                " [3, 1], [3, 2], [3, 3]]")

      self.room_kinder = Room.objects.get(name='Kinder', cinema=self.cinema_wiosna)

      # create some movie
      self.movie_wizard = Movie(title='Harry Potter', releaseDate='2017-02-12', length='123', producer='J. K. Rowling',
                           description='You\'re a wizard, Harry',
                           cover=File(open(BASE_DIR + '/test/static/wspawielkanocna.jpg', 'rb')))

      self.movie_wizard.save()
      self.movie_wizard.genre.add(self.horro)

      # create a showing
      Showing.objects.create(date='2018-12-23', hour='12:54:00', room=self.room_kinder,
                             movie=self.movie_wizard, audio_type=Showing.ORIGINAL, picture_type=Showing.TWO_DIM)

      self.showing_wizard1 = Showing.objects.get(date='2018-12-23', hour='12:54', room=self.room_kinder,
                             movie=self.movie_wizard, audio_type=Showing.ORIGINAL, picture_type=Showing.TWO_DIM)

      # create ticket types
      TicketType.objects.create(name='Ulgowy', price=12.59, description='Children below 18 years old and disabled')
      TicketType.objects.create(name='Normalny', price=59.12, description='Everyone else')

      self.ticket_type_ulgowy = TicketType.objects.get(name='Ulgowy', price=12.59,
                                                  description='Children below 18 years old and disabled')
      self.ticket_type_normalny = TicketType.objects.get(name='Normalny', price=59.12, description='Everyone else')

      # create some users and their profiles
      User.objects.create(username="elemelek", password='ulala')
      self.user_elemelek = User.objects.get(username="elemelek", password='ulala')

      User.objects.create(username="tabaluga", password='milusia')
      self.user_tabaluga = User.objects.get(username="tabaluga", password='milusia')

      ClientProfile.objects.create(user=self.user_elemelek, phone_number='880 111 533')
      self.user_profile_elemelek = ClientProfile.objects.get(user=self.user_elemelek, phone_number='880 111 533')

      EmployeeProfile.objects.create(user=self.user_tabaluga, cinema=self.cinema_lato)
      self.user_profile_tabaluga = EmployeeProfile.objects.get(user=self.user_tabaluga, cinema=self.cinema_lato)

    # in case something goes wrong in setUp() the covers of movies are not deleted
    except Exception as ee:
      print(ee)
      try:
        self.movie_wizard.delete()
      finally:
        raise ee

  # ######################
  def tearDown(self):

    # generally cleaning the database is not necessary as it will be deleted right after the tests

    try:

      # this loop should delete all the covers that were created during tests
      # this is not done automatically when deleting the movies
      for file in os.listdir(MEDIA_ROOT + "/covers"):
        if file not in self.__been_there_before:
          os.unlink(MEDIA_ROOT + "/covers/" + file)

      # this loop should delete all the thumbnails that were created during tests
      # this is not done automatically when deleting the movies
      for file in os.listdir(MEDIA_ROOT + "/thumbs"):
        if file not in self.__thumb_there_before:
          os.unlink(MEDIA_ROOT + "/thumbs/" + file)


    except Exception as e:
      print('An exception occured while cleaning up after tests.'
            '\nTake note, all tests run until now have passed.\n')
      print(e.__str__())


class NoTestOccuredException(Exception):
  """Exception used when an exception should have occured but it haven't happen"""
  pass


def check_adding_model_instance_with_wrong_fields(classname, error_message="", **kwargs):
  """Function used to run model creation for models that shouldn't be allowed
  in order to check if they are indeed not allowed"""
  try:
    if classname != Movie:
      classname.objects.create(**kwargs)

      raise NoTestOccuredException()
    else:
      f = classname(title=kwargs['title'], releaseDate=kwargs['Title'], length=kwargs['length'],
                    producer=kwargs['producer'], description=kwargs['description'],
                    cover=kwargs['cover'])

      f.save()
      f.genre.add(kwargs['genre'])
  except NoTestOccuredException as e:
    print(error_message)
    raise e
  except Exception as e:
    # print("Expected error occured. Info: " + e.__str__() + "\n\n\n")
    pass
