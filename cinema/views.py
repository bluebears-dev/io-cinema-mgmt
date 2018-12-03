from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Cinema
from cinema.serializers import CinemaSerializer


class CinemaListView(APIView):
  def get(self, request, format=None):
    cinema = Cinema.objects.all()
    serializer = CinemaSerializer(cinema, many=True)
    return Response(serializer.data)



def index(request):
  return render(request, 'index.html')
