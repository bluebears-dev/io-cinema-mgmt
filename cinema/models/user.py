##                                ##
##   ALL MODELS RELATED TO USER   ##
##                                ##
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

PHONE_NUMBER_REGEX = r'(\d{2} ?\d{3}(?: ?\d{2}){2})|' \
                     r'(\d{3}(?: \d{3}){2})'
"""
Matches number delimited space in three different formats:
  12 345 67 89
  123 456 789
  123456789
"""


class EmployeeProfile(models.Model):
    """
        Employee profile containing relevant data to cinema internals
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(verbose_name=_('Placówka'), to='Cinema', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return _('Dane pracownika')

    class Meta:
        verbose_name = _('Profil pracownika')
        verbose_name_plural = _('Profile pracownika')


class UserProfile(models.Model):
    """
        User profile containing non-auth data
    """

    # todo or not todo, depends, as for now many users can have the same phone number
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name=_('Numer telefonu'), max_length=12, unique=True, validators=[
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
