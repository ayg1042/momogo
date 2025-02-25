from django.urls import path
from . import views


app_name = 'websocket_api'

urlpatterns = [
    path('websocket_api/', views.index, name='webIndex'),
]