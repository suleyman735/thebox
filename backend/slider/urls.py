from rest_framework import routers
from .views import SliderViewSet

router = routers.DefaultRouter()
router.register(r'api/slider', SliderViewSet, 'Slider')


urlpatterns = router.urls