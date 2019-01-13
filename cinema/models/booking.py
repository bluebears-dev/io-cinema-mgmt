##                                    ##
##   ALL MODELS RELATED TO BOOKINGS   ##
##                                    ##

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class TicketType(models.Model):
    """
        Type and price of a ticket
    """

    ticketType = models.CharField(verbose_name=_('Typ biletu'), max_length=20, unique=True, db_column='type')
    price = models.DecimalField(verbose_name=_('Cena'), max_digits=6, decimal_places=2)
    description = models.TextField(verbose_name=_('Opis'), max_length=200)

    class Meta:
        verbose_name = _('Typ biletu')
        verbose_name_plural = _('Typy biletów')

    def __str__(self):
        return _('{0}'.format(self.ticketType))


class Ticket(models.Model):
    booking = models.ForeignKey(verbose_name=_('Rezerwacja'), to='Booking', on_delete=models.CASCADE)
    row = models.CharField(max_length=2)
    column = models.CharField(max_length=2)
    ticketType = models.ForeignKey(verbose_name=_('Typ biletu'), to='TicketType', db_column='type', null=True,
                                   on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('booking', 'row', 'column')
        verbose_name = _('Bilet')
        verbose_name_plural = _('Bilety')

    def __str__(self):
        return _('Bilet na {0}'.format(self.booking))


class Booking(models.Model):
    """
        Represents client's bookings and their states
    """
    INITIATED = 'Rozpoczęta'
    UNPAID = 'Nieopłacona'
    PAID = 'Opłacona'

    CHOICES_FOR_STATE = (
        (INITIATED, 'Rozpoczęta'),
        (UNPAID, 'Nieopłacona'),
        (PAID, 'Opłacona'),
    )

    user = models.ForeignKey(verbose_name=_('Klient'), to=User, on_delete=models.CASCADE, null=True)
    showing = models.ForeignKey(verbose_name=_('Seans'), to='Showing', on_delete=models.CASCADE)
    state = models.CharField(verbose_name=_('Stan rezerwacji'), max_length=20, choices=CHOICES_FOR_STATE,
                             default=INITIATED)
    finished = models.BooleanField(default=False)
    token = models.CharField(max_length=256)
    total_cost = models.DecimalField(verbose_name=_('Całkowity koszt'), max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('Rezerwacja')
        verbose_name_plural = _('Rezerwacje')

    def __str__(self):
        return _('Rezerwacja na {0}'.format(self.showing))
