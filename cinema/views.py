from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Cinema
from cinema.serializers import CinemaSerializer, CinemaBriefSerializer


class CinemaListView(APIView):
  def get(self, request, format=None):
    cinema = Cinema.objects.all()
    serializer = CinemaBriefSerializer(cinema, many=True)
    return Response(serializer.data)


class CinemaDetailsView(APIView):
  def _get(self, key):
    try:
      return Cinema.objects.get(pk=key)
    except Cinema.DoesNotExist:
      raise Http404

  def get(self, request, key, format=None):
    cinema = self._get(key)
    serializer = CinemaSerializer(cinema)
    return Response(serializer.data)


def index(request):
  return render(request, 'index.html')
