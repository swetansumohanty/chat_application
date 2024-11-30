from django.urls import path
from . import consumers

# websocket urls

ws_urlpatterns=[
    path('ws/sc/<str:groupname>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/<str:groupname>/',consumers.MyAsyncConsumer.as_asgi())
    
]
