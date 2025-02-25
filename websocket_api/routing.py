from django.urls import re_path
from websocket_api.consumers import ChatConsumer  # ✅ consumer 불러오기

websocket_urlpatterns = [
    re_path(r"^ws/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
]