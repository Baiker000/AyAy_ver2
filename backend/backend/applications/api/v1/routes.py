from rest_framework import routers
from backend.applications.api.v1.viewsets import GameViewSet


api_router = routers.SimpleRouter()
api_router.register('games', GameViewSet)