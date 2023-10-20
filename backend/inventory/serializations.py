from rest_framework import serializers
from .models import Product, TrainSchedule, Order, Bill


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class TrainScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainSchedule
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"
