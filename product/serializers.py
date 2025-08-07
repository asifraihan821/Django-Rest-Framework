from rest_framework import serializers
from decimal import Decimal
from product.models import Category,Product,Review



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


    
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),              #for hyperlink address for specific category
    #     view_name = "view-specific-category",

    # )

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax_price')

    def calculate_tax_price(self,product):
        return round(product.price * Decimal(1.1),2)
    
    def validate_price(self,price):
        if price < 0:
            raise serializers.ValidationError('Price could not be negetive')
        return price
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description']
        #view theke to product id paileo seta emni emni assign hobe na tai create methd k override kore review ta bosate hobe
    
    def create(self, validated_data):
        product_id = self.context['product_id'] #viewset theke context namei pabo tar moddhe product_id niye nilam
        return Review.objects.create(product_id=product_id,**validated_data) #review lekha object ta return korlam same id diye r baki data gula unpack kore pathai dilam jno review ta set hoi

