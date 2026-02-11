from django.urls import path
from . import views

urlpatterns = [
    path('series/<int:series_id>/latest/', views.series_latest, name='series_latest'),
]
