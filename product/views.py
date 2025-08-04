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
# Create your views here.


class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer


class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer



class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer