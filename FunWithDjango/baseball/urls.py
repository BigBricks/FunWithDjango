from rest_framework import routers
from .api import PlayerViewSet, TeamViewSet

router = routers.DefaultRouter()
router.register("api/baseball/players", PlayerViewSet, "players")
router.register("api/baseball/teams", TeamViewSet, "teams")

urlpatterns = router.urls
