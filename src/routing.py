from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import streakchat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(streakchat.routing.websocket_urlpatterns)),
})