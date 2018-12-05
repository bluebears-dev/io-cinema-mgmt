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
	"""
		Represents building location
	"""
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


class Showing(models.Model):
	"""
		Model representing showing in cinema
	"""
	DUBBING = 'Dubbing'
	ORIGINAL = 'Oryginalny'
	VOICE_OVER = 'Lektor'
	SUBTITLES = 'Napisy'

	AUDIO_CHOICES = (
		(DUBBING, 'Dubbing'),
		(ORIGINAL, 'Oryginalny'),
		(VOICE_OVER, 'Lektor'),
		(SUBTITLES, 'Napisy')
	)

	TWO_DIM = '2D'
	THREE_DIM = '3D'

	PICTURE_CHOICES = (
		(TWO_DIM, '2D'),
		(THREE_DIM, '3D')
	)

	date = models.DateField(verbose_name=_('Data seansu'))
	hour = models.TimeField(verbose_name=_('Godzina seansu'))
	room = models.ForeignKey(verbose_name=_('Sala'), to='Room', on_delete=models.CASCADE)
	movie = models.ForeignKey(verbose_name=_('Film'), to='Movie', on_delete=models.CASCADE)
	audio_type = models.CharField(verbose_name=_('Przekład'), max_length=10, choices=AUDIO_CHOICES)
	picture_type = models.CharField(verbose_name=_('Typ obrazu'), max_length=2, choices=PICTURE_CHOICES)

	class Meta:
		unique_together = ('room', 'hour', 'date')
		verbose_name = _('Seans')
		verbose_name_plural = _('Seanse')

	def __str__(self):
		return _('Seans {0} {1} : {2}'.format(self.date, self.hour, self.movie))


class Room(models.Model):
	"""
		Represents specific room in the cinema
	"""
	name = models.CharField(verbose_name=_('Nazwa'), max_length=20)
	cinema = models.ForeignKey(verbose_name=_('Kino'), to='Cinema', on_delete=models.CASCADE)

	class Meta:
		unique_together = (('name', 'cinema'),)
		verbose_name = _('Sala')
		verbose_name_plural = _('Sale')

	def __str__(self):
		return _('Sala {0} : {1}'.format(self.cinema, self.name))


class Seat(models.Model):  # details unknown yet
	room = models.ForeignKey(verbose_name=_('Sala'), to='Room', on_delete=models.CASCADE)
	# row = models.SmallIntegerField(verbose_name=_('Rząd w reprezentacji do wyświetlania'))
	# column = models.SmallIntegerField(verbose_name=_('Kolumna w reprezentacji do wyświetlania'))
	realRow = models.CharField(verbose_name=_('Numer rzędu'), max_length=2)
	realColumn = models.SmallIntegerField(verbose_name=_('Numer kolumny'))

	class Meta:
		# unique_together = ('room', 'row', 'column', 'realRow', 'realColumn')
		verbose_name = _('Miejsce')
		verbose_name_plural = _('Miejsca')

	def __str__(self):
		return _('Rząd {0}, kolumna {1}'.format(self.realRow, self.realColumn))
