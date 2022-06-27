from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, ApiViewSet, UserViewSet
router = SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'apis', ApiViewSet)
router.register(r'users', UserViewSet)
urlpatterns = router.urls
