from rest_framework import serializers
from .models import Product, Bill


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["ProductID", "product_name"]


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["BillID", "total_list_price"]
