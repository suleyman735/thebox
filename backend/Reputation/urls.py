from rest_framework import routers
from .views import ReputationsViewSet

router = routers.DefaultRouter()
router.register(r'api/reputation', ReputationsViewSet, 'Reputation')


urlpatterns = router.urls