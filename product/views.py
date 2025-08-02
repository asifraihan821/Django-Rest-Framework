from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Category,Product
from product.serializers import ProductSerializer,CategorySerializer
# Create your views here.


@api_view()
def view_specific_product(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)



@api_view()
def view_all_product(request):
    product = Product.objects.select_related('category').all()
    serializer = ProductSerializer(product, many=True,context={'request':request})
    return Response(serializer.data)



@api_view()
def view_category(request,pk):
    cat = get_object_or_404(Category,pk=pk)  
    serializer = CategorySerializer(cat)
    return Response(serializer.data)


@api_view()
def view_nothing(request):
    return Response({'message':'for Nothing in categories'})