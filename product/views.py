from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Category,Product
from product.serializers import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework import status
# Create your views here.


@api_view()
def view_specific_product(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)



@api_view(['GET','POST'])
def view_all_product(request):
    if request.method == 'GET':
        product = Product.objects.select_related('category').all()
        serializer = ProductSerializer(product, many=True,context={'request':request})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        print(serializer._validated_data)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view()
def view_specific_category(request,pk):
    cat = get_object_or_404(Category,pk=pk)  
    serializer = CategorySerializer(cat)
    return Response(serializer.data)


@api_view(['GET','POST'])
def view_categoreis(request):
    if request.method == 'GET':
        categories = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer._validated_data)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)