from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Category,Product
# Create your views here.


@api_view()
def view_product(request,id):
    try:
        product = Product.objects.get(pk=id)
        product_dict = {
            'id':product.id,'name':product.name,'price':product.price
        }
        return Response(product_dict)
    except Product.DoesNotExist:
        return Response({'message': 'Product Does not exist'},status=404)



@api_view()
def view_category(request):
    return Response({'message':'Categories'})

@api_view()
def view_nothing(request):
    return Response({'message':'for Nothing in categories'})