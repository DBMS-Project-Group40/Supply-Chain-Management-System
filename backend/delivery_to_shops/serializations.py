from rest_framework import serializers
from .models import ShopOrder, ShopDelivery


class ShopOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopOrder
        fields = "__all__"


class ShopDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDelivery
        fields = "__all__"
