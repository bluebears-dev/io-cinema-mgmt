from django.db import models
from django.utils.translation import gettext as _


# todo: zmienić MovieGenre jako pojedynczy gatunek
class MovieGenre(models.Model):

  name = models.CharField(max_length=30, verbose_name=_('Nazwa'), unique=True, null=False)

  class Meta:
    verbose_name = _('Gatunek')
    verbose_name_plural = _('Gatunki')

  def __str__(self):
    return _('{0}'.format(self.name))


class Movie(models.Model):
    """
		Model representing movie played at the cinema
    """
    title = models.CharField(max_length=100, verbose_name=_('Tytuł'))
    releaseDate = models.DateField(verbose_name=_('Data produkcji'))
    length = models.IntegerField(verbose_name=_('Czas trwania'))
    producer = models.CharField(max_length=50, verbose_name=_('Reżyseria'))
    description = models.TextField(verbose_name=_('Opis'))
    cover = models.ImageField(unique=True, max_length=200, verbose_name=_('Okładka'))
    genre = models.ManyToManyField(MovieGenre, db_column='genre')

    class Meta:
      unique_together = (("title", "producer"),)
      verbose_name = _('Film')
      verbose_name_plural = _('Filmy')

    def __str__(self):
      return _('{0}'.format(self.title))

    def delete(self, *args, **kwargs):
      # Delete cover file when removing movie record in base

      storage, path = self.cover.storage, self.cover.path
      # Delete the model before the file
      super(Movie, self).delete(*args, **kwargs)
      storage.delete(path)
