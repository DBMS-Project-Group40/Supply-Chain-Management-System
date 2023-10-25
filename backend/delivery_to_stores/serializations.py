from rest_framework import serializers
from .models import Store, Truck, TruckSchedule, TruckRoute, TruckGoods


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"


class TruckScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckSchedule
        fields = "__all__"


class TruckGoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckGoods
        fields = "__all__"
