from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description','product_count']
    product_count = serializers.IntegerField()


    product_count = serializers.SerializerMethodField(method_name='get_product_count')
                                        #query hitting too much
    def get_product_count(self,category):
        count = Product.objects.filter(category=category).count()
        return count


# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10,decimal_places=2,source='price')
#     stock = serializers.IntegerField()
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax_price')

#     """
#     1
#     category = serializers.PrimaryKeyRelatedField(
#         queryset = Category.objects.all()       #for all category listings.
#     )
#     """

#     """
#     2
#     category = serializers.StringRelatedField()      #for naming all the categories
#     """

#     """
#     3
#     category = CategorySerializer()      # for nested category serializing
    
#     """

#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),              #for hyperlink address for specific category
#         view_name = "view-specific-category",

#     )


 
#     def calculate_tax_price(self,product):
#         return round(product.price * Decimal(1.1),2)
    


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock','category','price_with_tax']


    
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),              #for hyperlink address for specific category
        view_name = "view-specific-category",

    )

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax_price')

    def calculate_tax_price(self,product):
        return round(product.price * Decimal(1.1),2)
    
    def validate_price(self,price):
        if price < 0:
            raise serializers.ValidationError('Price could not be negetive')
        return price