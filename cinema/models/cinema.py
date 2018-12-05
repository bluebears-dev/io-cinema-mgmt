##                                  ##
##   ALL MODELS RELATED TO CINEMA   ##
##                                  ##
from django.contrib import admin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from .user import PHONE_NUMBER_REGEX

POSTAL_CODE_REGEX = r'\d{2}-\d{3}'
"""
Matches postal code format:
  35-678
"""


class Cinema(models.Model):
  name = models.CharField(verbose_name=_('Nazwa kina'), max_length=100, unique=True)
  city = models.CharField(verbose_name=_('Miasto'), max_length=60, )
  address = models.CharField(verbose_name=_('Adres'), max_length=100)
  postal_code = models.CharField(verbose_name=_('Kod pocztowy'), max_length=6, validators=[
    RegexValidator(
      regex=POSTAL_CODE_REGEX,
      message=_('Wprowadż poprawny kod pocztowy.')
    )
  ])
  phone_number = models.CharField(verbose_name=_('Numer telefonu'), max_length=12, validators=[
    RegexValidator(
      regex=PHONE_NUMBER_REGEX,
      message=_('Wprowadź poprawny numer telefonu (może zawierać spacje).')
    )
  ])

  def __str__(self):
    return _('{0}'.format(self.name))

  class Meta:
    verbose_name = _('Kino')
    verbose_name_plural = _('Kina')


class Room(models.Model):
    """Represents a single room in some specified cinema"""

    name = models.CharField(verbose_name=_('Nazwa'), max_length=20)
    cinema = models.ForeignKey(verbose_name=_('Kino'), to='Cinema', on_delete=models.CASCADE)

    class Meta:
      unique_together = (('name', 'cinema'),)
      verbose_name = _('Sala')

    def __str__(self):
      return _('Sala {0} : {1}'.format(self.cinema, self.name))


class Seat(models.Model):  # details unknown yet
  room = models.ForeignKey(Room, models.CASCADE, verbose_name=_('Sala'))
  row = models.SmallIntegerField(verbose_name=_('Rząd w reprezentacji do wyświetlania'))
  column = models.SmallIntegerField(verbose_name=_('Kolumna w reprezentacji do wyświetlania'))
  realRow = models.SmallIntegerField(verbose_name=_('Numer rzędu'))
  realColumn = models.CharField(max_length=2, verbose_name=_('Numer kolumny'))

  class Meta:
    unique_together = ('room', 'row', 'column', 'realRow', 'realColumn')
    verbose_name = _('Miejsce')
    verbose_name_plural = _('Miejsca')

  def __str__(self):
    return _('Rząd {0}, kolumna {1}'.format(self.realRow, self.realColumn))


admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Seat)
