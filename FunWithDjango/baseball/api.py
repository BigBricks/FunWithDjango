from baseball.models import Team, Player
from rest_framework import viewsets, permissions
from .serializers import TeamSerializer, PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TeamSerializer
