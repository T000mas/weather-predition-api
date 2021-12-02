from django.urls import path

from . import views

urlpatterns = [
    path('getPredictionByCity/', views.getPredictionByCity.as_view(), name='getPredictionByCity'),
    path('getPredictionByCoordinates/', views.getPredictionByCoordinates.as_view(), name='getPredictionByCoordinates'),
]