
from duarteApp.api.views import AutomovilViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'automoviles', AutomovilViewSet, basename='automovil')

urlpatterns = router.urls
