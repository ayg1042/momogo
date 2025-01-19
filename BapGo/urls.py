from django.urls import path
from . import views

app_name = 'BapGo'


urlpatterns = [
    path('start/', views.start, name='start'),
    path('invite/', views.invite, name='invite'),
]