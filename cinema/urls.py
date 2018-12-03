from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('cinema/', views.CinemaListView.as_view()),
  path('prices/', views.TicketTypeView.as_view())
]
