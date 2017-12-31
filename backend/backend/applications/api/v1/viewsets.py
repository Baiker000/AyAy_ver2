from rest_framework import viewsets
from games.models import Game
from backend.applications.api.v1.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer