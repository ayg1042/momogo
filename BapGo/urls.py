from django.urls import path
from . import views

app_name = 'BapGo'


urlpatterns = [
    path('start/', views.start, name='start'),
    path("save-places/", views.save_kakao_data, name="save_kakao_data"),
    path('invite/', views.invite, name='invite'),
]