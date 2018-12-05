from django.db import models
from django.utils.translation import gettext as _
from django.contrib import admin


# todo ważne, jak już się będzie dało, zrób test, czy jak dodasz obraz i go usuniesz, to czy plik zostanie,
#  jeśli tak, to nadpisz metodę delete, żeby najpierw usuwało obraz, a dopiero później obiekt
class Movie(models.Model):
    """One set of values represents one movie"""

    title = models.TextField(verbose_name=_('Tytuł'))
    releaseDate = models.DateField(verbose_name=_('Data produkcji'))
    length = models.IntegerField(verbose_name=_('Czas trwania'))
    producer = models.TextField(verbose_name=_('Reżyseria'))
    description = models.TextField(null=True, blank=True, unique=True, verbose_name=_('Opis'))
    cover = models.ImageField(unique=True, max_length=200, verbose_name=_('Okładka'))

    class Meta:
        unique_together = (("title", "producer"),)
        verbose_name = _('Film')
        verbose_name_plural = _('Filmy')

    def __str__(self):
        return _('{0}'.format(self.title))


# todo: zmienić MovieGenre jako pojedynczy gatunek
class MovieGenre(models.Model):

    # choices for genre, should be set normal when the time is right
    G1 = 'gat1'
    G2 = 'gat2'
    HP = 'wiz'
    FB = 'lotr'
    HO = 'hor'
    KO = 'kom'
    LA = 'gat'
    UPS = 'ext'

    CHOICES_FOR_GENRE = (
      (G1, 'gatunek pierwszy'),
      (G2, 'gatunek drugi'),
      (HP, "you're a wizard, Harry"),
      (FB, 'you shall not pass'),
      (HO, 'sikasz ze strachu'),
      (KO, 'sikasz ze smiechu'),
      (LA, 'ostatni egzemplarz gatunków'),
      (UPS, 'extinction'),
    )

    # end choices

    """One movie can have more than one movie_genre but they should not be repeated"""
    movie = models.ForeignKey(Movie, models.CASCADE, verbose_name=_('Film'))
    genre = models.CharField(max_length=20, choices=CHOICES_FOR_GENRE, verbose_name=_('Gatunek'))

    class Meta:
        verbose_name = _('Gatunek')
        verbose_name_plural = _('Gatunki')

    def __str__(self):
        return _('{0} : {1}'.format(self.movie, self.genre))


admin.site.register(Movie)
admin.site.register(MovieGenre)
