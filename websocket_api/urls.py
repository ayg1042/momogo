from django.urls import path
from . import views


app_name = 'websocket_api'

urlpatterns = [
    path('', views.index, name='websocket_index'),
    path("chat_test/<str:room_name>", views.chatTest, name="chat_test"),
    path("chatReids/<str:room_name>", views.get_chat_room_users, name="get_chat"),    
    path('apiTest', views.apiTest, name='apiTets'),
]