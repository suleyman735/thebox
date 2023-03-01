from rest_framework import routers
from .views import AboutFrontViewSet,AboutExprienceViewSet,AboutHeaderViewSet

router = routers.DefaultRouter()
router.register(r'api/aboutfront', AboutFrontViewSet, 'About')
router.register(r'api/aboutexprience', AboutExprienceViewSet, 'About')
router.register(r'api/aboutheader', AboutHeaderViewSet, 'About')

urlpatterns = router.urls