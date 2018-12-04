from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

PHONE_NUMBER_REGEX = r'(\d{2} ?\d{3}(?: ?\d{2}){2})|' \
                     r'(\d{3}(?: \d{3}){2})'
"""
Matches number delimited space in three different formats:
  12 345 67 89
  123 456 789
  123456789
"""

POSTAL_CODE_REGEX = r'\d{2}-\d{3}'
"""
Matches postal code format:
  35-678
"""


class Movie(models.Model):
    """One set of values represents one movie"""

    title = models.TextField()
    releaseDate = models.DateField()
    length = models.IntegerField()
    producer = models.TextField()
    description = models.TextField(null=True, blank=True, unique=True)
    cover = models.ImageField(unique=True, max_length=200)                              # todo ważne, jak już się będzie dało, zrób test, czy jak dodasz obraz i go usuniesz, to czy plik zostanie, jeśli tak, to nadpisz metodę delete, żeby najpierw usuwało obraz, a dopiero później obiekt

    class Meta:
        # this means that the pair of those below must be unique
        unique_together = (("title", "releaseDate"),)


class MovieGenre(models.Model):
    """One movie can have more than one movie_genre but they should not be repeated"""
    movie = models.ForeignKey(Movie, models.CASCADE)
    genre = models.CharField(20, choices=(
      ('gat1', 'gatunek pierwszy'),
      ('gat2', 'gatunek drugi'),
      ('wiz', "you're a wizard, Harry"),
      ('lotr', 'you shall not pass'),
      ('hor', 'sikasz ze strachu'),
      ('kom', 'sikasz ze smiechu'),
      ('gat', 'ostatni gatunek'),
      ('ext', 'extinction'),
    ))


class TicketType(models.Model):
    """Represents kind of ticket

    One can consider changing the price to movie dependent version assuming there is time for that"""

    typo = models.CharField(max_length=20, primary_key=True, verbose_name=_('Typ biletu'), db_column='type')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Cena'))
    description = models.TextField(unique=True, verbose_name=_('Opis'), max_length=200)

    def __str__(self):
        return _('%(ticket_type)s' % {'ticket_type': self.typo})

    class Meta:
        verbose_name = _('Typ biletu')
        verbose_name_plural = _('Typy biletów')


# class Cinema(models.Model):
#    """Represents a single cinema unit"""

#    name = models.CharField(50, primary_key=True)
#    city = models.TextField()
#    postalCode = PostalCodeField()    # todo trzeba zrobić, not null, no default, no unique
#    address = models.TextField(unique=True)      # todo not null, no default, unique
#    phoneNumber = PhoneField()        # todo trzeba zrobić, not null, no default, unique


class Cinema(models.Model):
    name = models.CharField(verbose_name=_('Nazwa kina'), max_length=100, blank=False, unique=True)
    city = models.CharField(verbose_name=_('Miasto'), max_length=60, blank=False)
    address = models.CharField(verbose_name=_('Adres'), max_length=100, blank=False)
    postal_code = models.CharField(verbose_name=_('Kod pocztowy'), max_length=6, blank=False, validators=[
        RegexValidator(
            regex=POSTAL_CODE_REGEX,
            message=_('Wprowadż poprawny kod pocztowy')
        )
    ])
    phone_number = models.CharField(verbose_name=_('Numer telefonu'), max_length=12, blank=False, validators=[
        RegexValidator(
            regex=PHONE_NUMBER_REGEX,
            message=_('Wprowadź poprawny numer telefonu (może zawierać spacje).')
        )
    ])

    def __str__(self):
        return _('%(cinema)s' % {'cinema': self.name})

    class Meta:
        verbose_name = _('Kino')
        verbose_name_plural = _('Kina')


class Room(models.Model):
    """Represents a single room in some specified cinema"""

    name = models.CharField(2)
    cinema = models.ForeignKey(Cinema, models.CASCADE)

    class Meta:
        unique_together = (('name', 'cinema'),)


class Showing(models.Model):

    # Choices for audio type, should be corrected to normal when types are known
    # or else if just something sensible is needed before the deadline

    QUI = 'one'
    LLO = 'two'
    TTR = 'thr'
    CCT = 'czt'
    PPT = 'piat'
    INF = 'inf'

    AUDIO_CHOICES = (
      (QUI, 'quiet'),
      (LLO, 'loud'),
      (TTR, 'hard-bass'),
      (CCT, 'louder'),
      (PPT, 'LOUDER!!!!!1!1!!111!!1!!!1111'),
      (INF, 'the branch from "We Are Number One"'),
    )

    # choices for picture type
    NO = 'no'
    NN = 'nn'
    BW = 'bw'
    GO = 'go'
    GD = 'gd'
    D3 = 'd3'

    PICTURE_CHOICES = (
      (NO, 'black & white with gaussian distortion'),
      (NN, 'black & white with less gaussian distortion'),
      (BW, 'black & white'),
      (GO, 'colorful and dim'),
      (GD, 'colorful in hd'),
      (D3, 'colorful in 3D'),
    )

    """Represents a single spextacle"""
    date = models.DateField()
    hour = models.TimeField()
    room = models.ForeignKey(Room, models.CASCADE)
    movie = models.ForeignKey(Movie, models.CASCADE)
    audioType = models.CharField(10, choices=AUDIO_CHOICES)
    pictureType = models.CharField(2, choices=PICTURE_CHOICES)

    class Meta:
        unique_together = ('room', 'hour', 'date')


class UserProfile(models.Model):
    """
    User profile containing non-auth data
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name=_('Numer telefonu'), max_length=12, validators=[
        RegexValidator(
            regex=PHONE_NUMBER_REGEX,
            message=_('Wprowadź poprawny numer telefonu (może zawierać spacje).')
        )
    ])

    def __str__(self):
        return _('Dane kontaktowe')

    class Meta:
        verbose_name = _('Profil użytkownika')
        verbose_name_plural = _('Profile użytkownika')

# class User(models.Model):
#    email = models.EmailField(primary_key=True)
#    password = models.CharField(100)  # todo Ale to ma być hash jak coś, a ten komentarz tutaj to tylko tak żeby był
#    firstname = models.CharField(20)
#    surname = models.CharField(50)
#    phoneNumber = PhoneField()          # todo trzeba napisać, chyba null, no default, no unique
#    role = models.CharField(20, choices=(
#      ('admin', 'admin'),
#      ('kierownik', 'kierownik'),
#      ('redaktor', 'redaktor'),
#    ))


class Booking(models.Model):

    # Choices to be used
    FIRST = 'first_state'
    SECOND = 'second_state'
    THIRD = 'stety'

    CHOICES_FOR_STATE = (
      (FIRST, 'first_state'),
      (SECOND, 'second_state'),
      (THIRD, 'niestety'),
    )

    # end choices

    user = models.ForeignKey(User, models.CASCADE)
    showing = models.ForeignKey(Showing, models.CASCADE)
    state = models.CharField(20, choices=CHOICES_FOR_STATE, default='first_state')


class Seat(models.Model):   # details unknown yet
    room = models.ForeignKey(Room, models.CASCADE)
    row = models.SmallIntegerField()
    column = models.SmallIntegerField()
    realRow = models.SmallIntegerField()
    realColumn = models.CharField(2)

    class Meta:
        unique_together = ('room', 'row', 'column', 'realRow', 'realColumn')


class Ticket(models.Model):
    booking = models.ForeignKey(Booking, models.CASCADE)
    seat = models.ForeignKey(Seat, models.CASCADE)
    typo = models.ForeignKey(TicketType, models.CASCADE, verbose_name="type")

    class Meta:
        unique_together = ('booking', 'seat')
