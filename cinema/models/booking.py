##                                    ##
##   ALL MODELS RELATED TO BOOKINGS   ##
##                                    ##
from django.contrib import admin
from django.db import models
from django.utils.translation import gettext as _


class TicketType(models.Model):
  type = models.CharField(verbose_name=_('Typ biletu'), max_length=20, blank=False, unique=True)
  price = models.DecimalField(verbose_name=_('Cena'), max_digits=6, decimal_places=2, blank=False)
  description = models.TextField(verbose_name=_('Opis'), max_length=200, blank=False)

  def __str__(self):
    return _('%(ticket_type)s' % {'ticket_type': self.type})

  class Meta:
    verbose_name = _('Typ biletu')
    verbose_name_plural = _('Typy biletów')


admin.site.register(TicketType)
