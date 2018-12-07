from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cinema/', views.CinemaListView.as_view()),
    path('prices/', views.TicketTypeView.as_view()),
    path('showings/', views.ShowingView.as_view()),
    path('docs/', include_docs_urls(title='KAPPA Cinema API')),
]
