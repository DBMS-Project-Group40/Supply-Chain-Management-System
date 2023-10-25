from rest_framework import serializers
from .models import ShopOrder, ShopDelivery, TruckRoute


class ShopOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopOrder
        fields = "__all__"


class ShopDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopDelivery
        fields = "__all__"


class TruckRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckRoute
        fields = "__all__"
