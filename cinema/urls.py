from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('cinema/', views.CinemaListView.as_view()),
  path('cinema/<str:key>/', views.CinemaDetailsView.as_view()),
]
