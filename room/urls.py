from django.urls import path
from . import views

app_name = 'room'


urlpatterns = [
    path('member/', views.login, name='login'),
]