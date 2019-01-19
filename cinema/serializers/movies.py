
from rest_framework import serializers

from cinema.models import Movie, MovieGenre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover')
        read_only_fields = fields


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = ('name',)
        read_only_fields = fields


class MovieDetailsSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField('get_genres')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover', 'length', 'producer', 'description', 'releaseDate', 'genre')
        read_only_fields = fields

    def get_genres(self, obj):
        """
            Takes every object of genre and returns list of names
        :param obj:
        :return: list of genres
        """
        return [genre.name for genre in obj.genre.all()]
