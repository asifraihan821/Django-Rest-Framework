from django.urls import path,include
from rest_framework_nested import routers
from product.views import ProductViewSet,CategoryViewSet,ReviewViewSet

router = routers.DefaultRouter()
# router = simplerouter()
router.register('products',ProductViewSet, basename='product')
router.register('categories',CategoryViewSet)

product_router = routers.NestedDefaultRouter(router,'products',lookup='product')

product_router.register('reviews', ReviewViewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls))
] 