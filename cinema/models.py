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


# todo ewentualnie, można podopisywać helpy i error message, ale nie jest to teraz konieczne
class Movie(models.Model):
    """One set of values represents one movie"""

    title = models.TextField(verbose_name=_('Tytuł'))
    releaseDate = models.DateField(verbose_name=_('Data wydania'))
    length = models.IntegerField(verbose_name=_('Długość'))
    producer = models.TextField(verbose_name=_('Producent'))
    description = models.TextField(null=True, blank=True, unique=True, verbose_name=_('Opis'))
    cover = models.ImageField(unique=True, max_length=200, verbose_name=_('Okładka'))                              # todo ważne, jak już się będzie dało, zrób test, czy jak dodasz obraz i go usuniesz, to czy plik zostanie, jeśli tak, to nadpisz metodę delete, żeby najpierw usuwało obraz, a dopiero później obiekt

    class Meta:
        # this means that the pair of those below must be unique
        unique_together = (("title", "releaseDate"),)
        verbose_name = _('Film')
        verbose_name_plural = _('Filmy')


class MovieGenre(models.Model):

    # choices for genre, should be set normal when the time is right
    G1 = 'gat1'
    G2 = 'gat2'
    HP = 'wiz'
    FB = 'lotr'
    HO = 'hor'
    KO = 'kom'
    LA = 'gat'
    UPS = 'ext'

    CHOICES_FOR_GENRE = (
      (G1, 'gatunek pierwszy'),
      (G2, 'gatunek drugi'),
      (HP, "you're a wizard, Harry"),
      (FB, 'you shall not pass'),
      (HO, 'sikasz ze strachu'),
      (KO, 'sikasz ze smiechu'),
      (LA, 'ostatni egzemplarz gatunków'),
      (UPS, 'extinction'),
    )

    # end choices

    """One movie can have more than one movie_genre but they should not be repeated"""
    movie = models.ForeignKey(Movie, models.CASCADE, verbose_name=_('Film'))
    genre = models.CharField(20, choices=CHOICES_FOR_GENRE, verbose_name=_('Gatunek'))

    class Meta:
        verbose_name = _('Gatunek')
        verbose_name_plural = _('Gatunki')


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

    name = models.CharField(2, verbose_name=_('Nazwa'))
    cinema = models.ForeignKey(Cinema, models.CASCADE, verbose_name=_('Kino'))

    class Meta:
        unique_together = (('name', 'cinema'),)
        verbose_name_plural = _('Sale')
        verbose_name = _('Sala')


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
    date = models.DateField(verbose_name=_('Data'))
    hour = models.TimeField(verbose_name=_('Godzina'))
    room = models.ForeignKey(Room, models.CASCADE, verbose_name=_('Sala'))
    movie = models.ForeignKey(Movie, models.CASCADE, verbose_name=_('Film'))
    audioType = models.CharField(10, choices=AUDIO_CHOICES, verbose_name=_('Jakość dźwięku'))
    pictureType = models.CharField(2, choices=PICTURE_CHOICES, verbose_name=_('Jakość obrazu'))

    class Meta:
        unique_together = ('room', 'hour', 'date')
        verbose_name = _('Seans')
        verbose_name_plural = _('Seanse')


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

    user = models.ForeignKey(UserProfile, models.CASCADE, verbose_name=_('Profil użytkownika'))
    showing = models.ForeignKey(Showing, models.CASCADE, verbose_name=_('Seans'))
    state = models.CharField(20, choices=CHOICES_FOR_STATE, default='first_state',verbose_name=_('Stan'))

    class Meta:
        verbose_name = _('Rezerwacja')
        verbose_name_plural = _('Rezerwacje')


class Seat(models.Model):   # details unknown yet
    room = models.ForeignKey(Room, models.CASCADE, verbose_name=_('Sala'))
    row = models.SmallIntegerField(verbose_name=_('Rząd w reprezentacji do wyświetlania'))
    column = models.SmallIntegerField(verbose_name=_('Kolumna w reprezentacji do wyświetlania'))
    realRow = models.SmallIntegerField(verbose_name=_('Numer rzędu'))
    realColumn = models.CharField(2, verbose_name=_('Numer kolumny'))

    class Meta:
        unique_together = ('room', 'row', 'column', 'realRow', 'realColumn')
        verbose_name = _('Miejsce')
        verbose_name_plural = _('Miejsca')


class Ticket(models.Model):
    booking = models.ForeignKey(Booking, models.CASCADE, verbose_name=_('Rezerwacja'))
    seat = models.ForeignKey(Seat, models.CASCADE, verbose_name=_('Miejsce'))
    typo = models.ForeignKey(TicketType, models.CASCADE, verbose_name=_('Typ biletu'))

    class Meta:
        unique_together = ('booking', 'seat')
        verbose_name = _('Bilet')
        verbose_name_plural = _('Bilety')
