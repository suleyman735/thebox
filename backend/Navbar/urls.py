from rest_framework import routers
from .views import NavbarLogoViewSet,NavbarMenuViewSet

router = routers.DefaultRouter()
router.register(r'api/navbarlogo', NavbarLogoViewSet, 'Navbar')
router.register(r'api/navbarmenu', NavbarMenuViewSet, 'Navbar')

urlpatterns = router.urls