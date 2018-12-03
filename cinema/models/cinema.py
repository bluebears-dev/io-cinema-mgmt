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


admin.site.register(Cinema)
