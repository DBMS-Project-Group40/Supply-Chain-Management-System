from rest_framework import serializers
from .models import Product, Bill


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name", "price", "stock_count"]


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["product"]
