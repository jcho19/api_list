from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, ApiViewSet, UserViewSet
router = SimpleRouter()
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'apis', ApiViewSet, 'apis')
router.register(r'users', UserViewSet, 'users')
urlpatterns = router.urls
