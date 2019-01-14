from django.urls import path
from rest_framework.documentation import include_docs_urls

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('docs/', include_docs_urls(title='KAPPA Cinema API')),
    path('cinemas/', views.CinemaListView.as_view()),
    path('prices/', views.TicketTypeView.as_view()),
    path('showings/<int:showing_id>', views.ShowingView.as_view()),
    path('<int:cinema_id>/<int:movie_id>/<str:date>/showings', views.ShowingListView.as_view()),
    path('<int:cinema_id>/<str:date>/movies', views.MoviesView.as_view()),
    path('movies/<int:movie_id>/', views.MovieDetailsView.as_view()),
    path('rooms/<int:room_id>/', views.RoomView.as_view()),
    path('showings/<int:showing_id>/book/', views.book_showing),
    path('bookings/<int:booking_id>', views.cancel_booking),
    path('bookings/<int:booking_id>/tickets', views.replace_tickets)
]
