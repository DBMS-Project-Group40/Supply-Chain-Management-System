from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Store, Truck, TruckSchedule, TruckGoods
from .serializations import (
    StoreSerializer,
    TruckSerializer,
    TruckScheduleSerializer,
    TruckRouteSerializer,
    TruckGoodsSerializer,
)


@api_view(["GET", "POST"])
def store_list(request):
    if request.method == "GET":
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def store_detail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    if request.method == "GET":
        serializer = StoreSerializer(store)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
