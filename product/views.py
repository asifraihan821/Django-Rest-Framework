from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Category,Product
# Create your views here.


@api_view()
def view_product(request,id):
    product = get_object_or_404(Product,pk=id)
    product_dict = {
        'id':product.id,'name':product.name,'price':product.price
    }
    return Response(product_dict)



@api_view()
def view_category(request,id):
    cat = get_object_or_404(Category,pk=id)  # get_object_of_404 takes the model name and pk argument as argument
    cat_dict = {'name':cat.name,'des':cat.description}
    return Response(cat_dict)


@api_view()
def view_nothing(request):
    return Response({'message':'for Nothing in categories'})