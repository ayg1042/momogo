"""
ASGI config for momogo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from websocket_api.routing import websocket_urlpatterns



import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'momogo.settings')
django.setup()  # Django 초기화 (WebSocket 연결을 위해 필요)

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # WebSocket URL 패턴 적용
        )
    ),
})

