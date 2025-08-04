from django.urls import path
from product import views



urlpatterns = [
    path('<int:id>/',views.ViewSpecificProduct.as_view(),name='specific-product'),
    path('',views.ProductList.as_view(),name='product-list'),
    
]
