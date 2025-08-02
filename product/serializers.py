from rest_framework import serializers
from decimal import Decimal


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=10,decimal_places=2,source='price')
    stock = serializers.IntegerField()

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax_price')

    def calculate_tax_price(self,product):
        return round(product.price * Decimal(1.1),2)