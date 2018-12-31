import os
from functools import partial
from io import BytesIO
from uuid import uuid4

from PIL import Image
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.images import ImageFile
from django.core.files.storage import default_storage
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

COVER_PATH = 'covers/'


def image_filename(instance, filename, catalog):
    """
        Function that returns path with random filename for image.
        Image will be created at /media/{catalog}/ path.
        It should be used together with partial for catalog setting.
    """
    extension = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid4().hex, extension)
    return os.path.join(catalog, filename)


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
        upload_to=partial(image_filename, catalog=COVER_PATH)
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

    all_genres.short_description = _('Gatunki')

    def delete_file(self):
        """
            Try to delete image for specific movie
        :return:
        """
        try:
            movie = Movie.objects.get(id=self.id)
            filename = os.path.split(movie.cover.name)[-1]
            movie.cover.delete(False)
            default_storage.delete(os.path.join('thumbs', filename))
        except ObjectDoesNotExist or FileNotFoundError:
            pass

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.delete_file()
        super(Movie, self).save()
        cover_file = default_storage.open(self.cover.name, 'r+b')
        image = Image.open(cover_file)
        image.thumbnail((600, 600), Image.BICUBIC)
        image.save(cover_file, 'JPEG', quality=90)
        cover_file.close()

        filename = os.path.split(self.cover.name)[-1]
        content = BytesIO()
        image.thumbnail((100, 100), Image.BILINEAR)
        image.save(content, "JPEG", quality=90)
        content.seek(0)

        # Save image thumbnail
        thumb_file = default_storage.open(os.path.join('thumbs', filename), 'wb')
        thumb_file.write(content.getvalue())
        thumb_file.close()

    def delete(self, using=None, keep_parents=False):
        self.delete_file()
        super(Movie, self).delete()


class MovieGenre(models.Model):
    """
        Model for movie genres
    """
    name = models.CharField(verbose_name=_('Nazwa gatunku'), max_length=30, unique=True)

    class Meta:
        verbose_name = _('Gatunek')
        verbose_name_plural = _('Gatunki')

    def __str__(self):
        return _('{0}'.format(self.name))
