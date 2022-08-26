from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet,ProductGenericViewSet


router = DefaultRouter()

# router.register('product',ProductGenericViewSet,basename='Products')
router.register('product',ProductViewSet,basename='Products')


urlpatterns = router.urls