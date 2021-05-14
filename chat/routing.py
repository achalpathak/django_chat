from django.urls import path
from . import consumers

websocket_urls = [path("websocket/<str:room_name>/", consumers.ChatConsumer.as_asgi())]
