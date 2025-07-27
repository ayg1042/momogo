from django.urls import path
from . import views

app_name = 'roomDetail'


urlpatterns = [
    path('member/', views.login, name='login'),
    path('invite/', views.add_members, name='invite'),
]