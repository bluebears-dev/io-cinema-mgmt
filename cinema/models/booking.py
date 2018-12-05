##                                    ##
##   ALL MODELS RELATED TO BOOKINGS   ##
##                                    ##

from django.contrib import admin
from django.db import models
from django.utils.translation import gettext as _


class TicketType(models.Model):
  ticketType = models.CharField(verbose_name=_('Typ biletu'), max_length=20, unique=True, db_column='type')
  price = models.DecimalField(verbose_name=_('Cena'), max_digits=6, decimal_places=2)
  description = models.TextField(verbose_name=_('Opis'), max_length=200)

  class Meta:
    verbose_name = _('Typ biletu')
    verbose_name_plural = _('Typy biletów')

  def __str__(self):
    return _('{0}'.format(self.ticketType))


class Showing(models.Model):
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

    date = models.DateField(verbose_name=_('Data seansu'))
    hour = models.TimeField(verbose_name=_('Godzina seansu'))
    room = models.ForeignKey(verbose_name=_('Sala'), to='Room', on_delete=models.CASCADE)
    movie = models.ForeignKey(verbose_name=_('Film'), to='Movie', on_delete=models.CASCADE)
    audioType = models.CharField(verbose_name=_('Przekład'), max_length=10, choices=AUDIO_CHOICES)
    pictureType = models.CharField(verbose_name=_('Typ obrazu'), max_length=2, choices=PICTURE_CHOICES)

    class Meta:
      unique_together = ('room', 'hour', 'date')
      verbose_name = _('Seans')
      verbose_name_plural = _('Seanse')

    def __str__(self):
      return _('Seans {0} {1} : {2}'.format(self.date, self.hour, self.movie))


class Booking(models.Model):
    FIRST = 'first_state'
    SECOND = 'second_state'
    THIRD = 'stety'

    CHOICES_FOR_STATE = (
      (FIRST, 'first_state'),
      (SECOND, 'second_state'),
      (THIRD, 'niestety'),
    )

    user = models.ForeignKey(verbose_name=_('Klient'), to='User', on_delete=models.CASCADE)
    showing = models.ForeignKey(verbose_name=_('Seans'), to='Showing', on_delete=models.CASCADE)
    state = models.CharField(verbose_name=_('Stan rezerwacji'), max_length=20, choices=CHOICES_FOR_STATE, default='first_state')

    class Meta:
      verbose_name = _('Rezerwacja')
      verbose_name_plural = _('Rezerwacje')

    def __str__(self):
      return _('Rezerwacja na {0}'.format(self.showing))


class Ticket(models.Model):
  booking = models.ForeignKey(verbose_name=_('Rezerwacja'), to='Booking', on_delete=models.CASCADE)
  seat = models.ForeignKey(verbose_name=_('Miejsce'), to='Seat', on_delete=models.CASCADE)
  ticketType = models.ForeignKey(verbose_name=_('Typ biletu'), to='TicketType', on_delete=models.CASCADE, db_column='type')

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
