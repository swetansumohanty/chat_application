"""
ASGI config for wechat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from app.consumers import MyAsyncConsumer
from chat.consumers import PersonalChatConsumer
from django.urls import path
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wechat.settings')
django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/ac/<str:groupname>/',MyAsyncConsumer.as_asgi()),
                path('ac/<int:id>/',PersonalChatConsumer.as_asgi()),
            ])
        )
    ),
})

