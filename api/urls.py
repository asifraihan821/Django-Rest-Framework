from django.urls import path,include
from product import views
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet,CategoryViewSet

router = DefaultRouter()
# router = simplerouter()
router.register('products',ProductViewSet)
router.register('categories',CategoryViewSet)

urlpatterns = router.urls