##                                ##
##   ALL MODELS RELATED TO USER   ##
##                                ##
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _


PHONE_NUMBER_REGEX = r'(\d{2} ?\d{3}(?: ?\d{2}){2})|' \
                     r'(\d{3}(?: \d{3}){2})'
"""
Matches number delimited space in three different formats:
  12 345 67 89
  123 456 789
  123456789
"""


class Client(User):
    """
        Proxy model for isolation of Clients inside admin panel
    """

    class Meta:
        app_label = 'auth'
        proxy = True
        verbose_name = _('Klient')
        verbose_name_plural = _('Klienci')


class Editor(User):
    """
        Proxy model for Editor type role
    """

    class Meta:
        app_label = 'auth'
        proxy = True
        verbose_name = _('Redaktor')
        verbose_name_plural = _('Redaktorzy')


class Director(User):
    """
        Proxy model for Director type role
    """

    class Meta:
        app_label = 'auth'
        proxy = True
        verbose_name = _('Kierownik')
        verbose_name_plural = _('Kierownictwo')


class Admin(User):
    """
        Proxy model for Admin type role
    """

    class Meta:
        app_label = 'auth'
        proxy = True
        verbose_name = _('Administrator')
        verbose_name_plural = _('Administratorzy')


class EmployeeProfile(models.Model):
    """
        Employee profile containing relevant data to cinema internals
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    cinema = models.ForeignKey(verbose_name=_('Placówka'), to='Cinema', on_delete=models.CASCADE)

    def __str__(self):
        return _('{0}'.format(self.cinema.name))

    class Meta:
        verbose_name = _('Profil pracownika')
        verbose_name_plural = _('Profile pracownika')


class ClientProfile(models.Model):
    """
        User profile containing non-auth data
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
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
