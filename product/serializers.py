from rest_framework import serializers
from decimal import Decimal
from product.models import Category



class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=10,decimal_places=2,source='price')
    stock = serializers.IntegerField()
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax_price')

    """
    1
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all()       #for all category listings.
    )
    """

    """
    2
    category = serializers.StringRelatedField()      #for naming all the categories
    """

    """
    3
    category = CategorySerializer()      # for nested category serializing
    
    """

    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),              #for hyperlink address for specific category
        view_name = "view-specific-category",

    )


 
    def calculate_tax_price(self,product):
        return round(product.price * Decimal(1.1),2)
    

