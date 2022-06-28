from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, ApiViewSet, UserViewSet
router = SimpleRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'apis', ApiViewSet, basename='apis')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls
