from rest_framework import serializers
from .models import Product, Bill


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_id", "product_name", "bill_id"]


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["bill_id", "total_list_price"]
