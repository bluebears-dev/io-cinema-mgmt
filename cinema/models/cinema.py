#                                  #
#   ALL MODELS RELATED TO CINEMA   #
#                                  #
import datetime
import json
import re

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

    def _check_collision(self, new_show):
        """
            Check if two showings are not colliding with each other
        :param new_show: show added by user
        :return:
        """
        from django.core.exceptions import ValidationError
        new_show_start = datetime.datetime.combine(datetime.date.today(), new_show.hour)
        show_start = datetime.datetime.combine(datetime.date.today(), self.hour)

        if not (new_show_start + datetime.timedelta(minutes=new_show.movie.length) <= show_start
                or show_start + datetime.timedelta(minutes=self.movie.length) <= new_show_start):
            raise ValidationError(_('Dodawany seans koliduje z istniejącym ({0})'.format(new_show)))

    def clean(self):
        if hasattr(self, 'room') and hasattr(self, 'date') and hasattr(self, 'movie'):
            showings = Showing.objects.filter(room=self.room, date=self.date)
            for show in showings:
                self._check_collision(show)
        super().clean()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_clean()
        super().save(force_insert=False, force_update=False, using=None,
                     update_fields=None)

    def __str__(self):
        return _('{2} ({0} {1})'.format(self.date, self.hour, self.movie))

    class Meta:
        unique_together = ('room', 'hour', 'date')
        verbose_name = _('Seans')
        verbose_name_plural = _('Seanse')


def max_or_value(arr, val):
    if arr and len(arr):
        return max(arr)
    else:
        return val


class Seat(models.Model):  # details unknown yet
    room = models.ForeignKey(verbose_name=_('Sala'), to='Room', on_delete=models.CASCADE)
    realRow = models.SmallIntegerField(verbose_name=_('Numer rzędu'))
    realColumn = models.SmallIntegerField(verbose_name=_('Numer kolumny'))

    class Meta:
        verbose_name = _('Miejsce')
        verbose_name_plural = _('Miejsca')

    def __str__(self):
        return _('Rząd {0}, kolumna {1}'.format(self.realRow, self.realColumn))


class Room(models.Model):
  """
      Represents specific room in the cinema
  """
  name = models.CharField(verbose_name=_('Nazwa'), max_length=20)
  cinema = models.ForeignKey(verbose_name=_('Kino'), to='Cinema', on_delete=models.CASCADE)
  rows = models.IntegerField()
  cols = models.IntegerField()
  json_layout = models.TextField(default="[[1, 1]]")

  @property
  def layout(self):
    """
        Return parsed array representing layout.
        Its a list containing tuples:
            (row, col)
    """
    try:
      layout = json.loads(self.json_layout)
      return layout
    except TypeError:
      return None

  @property
  def raw_layout(self):
    """
        Returns flattened indices of layout matrix
    """
    layout = self.layout
    cols = self.cols
    raw_data = map(lambda v: (v[0] - 1) * cols + v[1] - 1, layout)
    return list(raw_data)

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    for str in re.findall(r"\[.*?]", self.json_layout):
      patt = re.search(r"\[([0-9]+), ([0-9]+)]", str)
      row = patt.group(1)
      col = patt.group(2)
      Seat.objects.create(room=self, realRow=int(row), realColumn=int(col))

  class Meta:
    unique_together = (('name', 'cinema'),)
    verbose_name = _('Sala')
    verbose_name_plural = _('Sale')

  def __str__(self):
    return _('{1} ({0})'.format(self.cinema, self.name))
