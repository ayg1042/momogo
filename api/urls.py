from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('mapApiData/', views.mapApiData, name='mapApiData'),
]