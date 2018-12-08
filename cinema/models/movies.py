import os
from uuid import uuid4
from django.core.exceptions import ObjectDoesNotExist
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
    filename = '{}.{}'.format(uuid4().hex, extension)
    return os.path.join(PATH, filename)


class Movie(models.Model):
    """
        Model representing movie played at the cinema
    """
    title = models.CharField(verbose_name=_('Tytuł'), max_length=100)
    releaseDate = models.DateField(verbose_name=_('Data produkcji'))
    length = models.IntegerField(verbose_name=_('Czas trwania'))
    producer = models.CharField(verbose_name=_('Reżyseria'), max_length=50)
    description = models.TextField(verbose_name=_('Opis'))
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

    def delete_file(self):
        """
            Try to delete image for specififc movie
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

# # todo: zmienić MovieGenre jako pojedynczy gatunek
# class MovieGenre(models.Model):
# 	G1 = 'gat1'
# 	G2 = 'gat2'
# 	HP = 'wiz'
# 	FB = 'lotr'
# 	HO = 'hor'
# 	KO = 'kom'
# 	LA = 'gat'
# 	UPS = 'ext'
#
# 	CHOICES_FOR_GENRE = (
# 		(G1, 'gatunek pierwszy'),
# 		(G2, 'gatunek drugi'),
# 		(HP, "you're a wizard, Harry"),
# 		(FB, 'you shall not pass'),
# 		(HO, 'sikasz ze strachu'),
# 		(KO, 'sikasz ze smiechu'),
# 		(LA, 'ostatni egzemplarz gatunków'),
# 		(UPS, 'extinction'),
# 	)
#
# 	# end choices
#
# 	"""One movie can have more than one movie_genre but they should not be repeated"""
# 	movie = models.ForeignKey(Movie, models.CASCADE, verbose_name=_('Film'))
# 	genre = models.CharField(max_length=20, choices=CHOICES_FOR_GENRE, verbose_name=_('Gatunek'))
#
# 	class Meta:
# 		verbose_name = _('Gatunek')
# 		verbose_name_plural = _('Gatunki')
#
# 	def __str__(self):
# 		return _('{0} : {1}'.format(self.movie, self.genre))
