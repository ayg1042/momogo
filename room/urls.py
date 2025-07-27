from django.urls import path
from . import views

app_name = 'room'


urlpatterns = [
    path('member/', views.login, name='login'),
    path('api/create/', views.create_room, name='create_room'),
    path('', views.room_page, name='room_page')
]