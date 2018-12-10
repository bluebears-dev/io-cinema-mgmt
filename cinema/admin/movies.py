from django.contrib import admin

from cinema.models import Movie, MovieGenre


class MovieAdmin(admin.ModelAdmin):
    """
        Movie list with filtering
    """

    list_display = ('title', 'releaseDate', 'producer', 'length', 'all_genres')
    list_filter = ('releaseDate', 'producer',)


class MovieGenreAdmin(admin.ModelAdmin):
    """
        Movie genre display
    """
    list_display = ('name',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieGenre, MovieGenreAdmin)
