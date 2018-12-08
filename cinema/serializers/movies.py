from cinema.models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'cover')
        read_only_fields = fields
