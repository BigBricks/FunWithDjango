from rest_framework import routers
from .api import PlayerViewSet

router = routers.DefaultRouter()
router.register("api/baseball", PlayerViewSet, "baseball")

urlpatterns = router.urls
