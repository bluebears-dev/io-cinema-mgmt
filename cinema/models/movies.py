import os
from uuid import uuid4
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

PATH = 'covers/'


def image_filename(instance, filename):
    """
        Generates a function that returns path with random filename for image

    :param path: Special path inside static/ folder
    :return: Function for upload_to that returns path of the image
    """
    extension = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid4().hex, extension)
    return os.path.join(PATH, filename)


class Movie(models.Model):
    """
        Model representing movie played at the cinema
    """
    title = models.CharField(verbose_name=_('Tytuł'), max_length=100)
    releaseDate = models.DateField(verbose_name=_('Data produkcji'))
    length = models.IntegerField(verbose_name=_('Czas trwania'), validators=[
        MinValueValidator(1)
    ])
    producer = models.CharField(verbose_name=_('Reżyseria'), max_length=50)
    description = models.TextField(verbose_name=_('Opis'))
    genre = models.ManyToManyField(verbose_name=_('Gatunek'), to='MovieGenre')
    cover = models.ImageField(
        verbose_name=_('Okładka'),
        unique=True,
        upload_to=image_filename
    )

    class Meta:
        unique_together = (("title", "producer"),)
        verbose_name = _('Film')
        verbose_name_plural = _('Filmy')

    def __str__(self):
        return _('{0}'.format(self.title))

    def all_genres(self):
        """
            Return name of all genres for list display
        :return: Coma delimited genre names
        """
        return ', '.join([g.name for g in self.genre.all()])

    def delete_file(self):
        """
            Try to delete image for specific movie
        :return:
        """
        try:
            movie = Movie.objects.get(id=self.id)
            movie.cover.delete(False)
        except ObjectDoesNotExist:
            pass

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.delete_file()
        super(Movie, self).save()

    def delete(self, using=None, keep_parents=False):
        self.delete_file()
        super(Movie, self).delete()


class MovieGenre(models.Model):
    """
        Model for movie genres
    """
    name = models.CharField(verbose_name=_('Nazwa gatunku'), max_length=30)

    class Meta:
        verbose_name = _('Gatunek')
        verbose_name_plural = _('Gatunki')

    def __str__(self):
        return _('{0}'.format(self.name))
