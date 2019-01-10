from django.urls import path
from rest_framework.documentation import include_docs_urls

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docs/', include_docs_urls(title='KAPPA Cinema API')),
    path('cinema/', views.CinemaListView.as_view()),
    path('prices/', views.TicketTypeView.as_view()),
    path('showings/<int:cinema>/<int:id>/<str:date>', views.ShowingView.as_view()),
    path('movies/<int:cinema>/<str:date>', views.MoviesView.as_view()),
    path('movie/<int:id>/', views.MovieDetailsView.as_view()),
    path('room/<int:showing_id>/', views.RoomView.as_view())
]
