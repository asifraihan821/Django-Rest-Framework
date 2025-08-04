from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Category,Product
from product.serializers import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 10:
            return Response('product with stock more than 10 could not be deleted')
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer

