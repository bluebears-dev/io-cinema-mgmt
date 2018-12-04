##                                    ##
##   ALL MODELS RELATED TO BOOKINGS   ##
##                                    ##

from django.contrib import admin
from django.db import models
from django.utils.translation import gettext as _
from .cinema import Room, Seat
from .movies import Movie
from django.contrib.auth.models import User


class TicketType(models.Model):
  """Represents kind of ticket

  One can consider changing the price to movie dependent version assuming there is time for that"""

  typo = models.CharField(max_length=20, primary_key=True, verbose_name=_('Typ biletu'), db_column='type')
  price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Cena'))
  description = models.TextField(unique=True, verbose_name=_('Opis'), max_length=200)

  class Meta:
    verbose_name = _('Typ biletu')
    verbose_name_plural = _('Typy biletów')

  def __str__(self):
    return _('{0}'.format(self.typo))


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
    audioType = models.CharField(max_length=10, choices=AUDIO_CHOICES, verbose_name=_('Jakość dźwięku'))
    pictureType = models.CharField(max_length=2, choices=PICTURE_CHOICES, verbose_name=_('Jakość obrazu'))

    class Meta:
      unique_together = ('room', 'hour', 'date')
      verbose_name = _('Seans')
      verbose_name_plural = _('Seanse')

    def __str__(self):
      return _('Seans {0} {1} : {2}'.format(self.date, self.hour, self.movie))


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

    user = models.ForeignKey(User, models.CASCADE, verbose_name=_('Profil użytkownika'))
    showing = models.ForeignKey(Showing, models.CASCADE, verbose_name=_('Seans'))
    state = models.CharField(max_length=20, choices=CHOICES_FOR_STATE, default='first_state', verbose_name=_('Stan'))

    class Meta:
      verbose_name = _('Rezerwacja')
      verbose_name_plural = _('Rezerwacje')

    def __str__(self):
      return _('Rezerwacja na {0}'.format(self.showing))


class Ticket(models.Model):
  booking = models.ForeignKey(Booking, models.CASCADE, verbose_name=_('Rezerwacja'))
  seat = models.ForeignKey(Seat, models.CASCADE, verbose_name=_('Miejsce'))
  typo = models.ForeignKey(TicketType, models.CASCADE, verbose_name=_('Typ biletu'), db_column='type')

  class Meta:
    unique_together = ('booking', 'seat')
    verbose_name = _('Bilet')
    verbose_name_plural = _('Bilety')

  def __str__(self):
    return _('Bilet na {0}'.format(self.booking))


admin.site.register(TicketType)
admin.site.register(Showing)
admin.site.register(Booking)
admin.site.register(Ticket)
