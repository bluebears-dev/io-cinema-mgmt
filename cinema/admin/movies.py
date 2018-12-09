from django.contrib import admin

from cinema.models import Movie


class MovieAdmin(admin.ModelAdmin):
    """
        Movie list with filtering
    """

    list_display = ('title', 'releaseDate', 'producer', 'length')
    list_filter = ('releaseDate', 'producer')


admin.site.register(Movie, MovieAdmin)
