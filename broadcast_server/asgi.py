"""
ASGI config for broadcast_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from broadcast import routing
import redis


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'broadcast_server.settings')


r = redis.Redis()
r.delete('connected_clients')
for key in r.scan_iter('client:*'):
    r.delete(key)
print('Redis cleaned on ASGI startup')


application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
        routing.websocket_urlpatterns
        )
    )
})
