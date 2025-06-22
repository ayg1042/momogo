from django.urls import path
from . import views

app_name = 'member'


urlpatterns = [
    path('member/', views.login, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout, name='logout'),
]