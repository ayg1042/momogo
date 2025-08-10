from django.urls import path
from . import views

app_name = 'member'


urlpatterns = [
    path('member/', views.login, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('members/', views.list_page, name='member_list_page'),
    path('api/members/', views.getMembers, name='member_list_api'),
]