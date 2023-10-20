from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Store, Truck, TruckSchedule, TruckRoute, TruckGoods
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


@api_view(["GET", "POST"])
def truck_list(request):
    if request.method == "GET":
        queryset = Truck.objects.all()
        serializer = TruckSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def truck_detail(request, slug):
    truck = get_object_or_404(Truck, slug=slug)
    if request.method == "GET":
        serializer = TruckSerializer(truck)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def truck_schedule_list(request):
    if request.method == "GET":
        queryset = TruckSchedule.objects.all()
        serializer = TruckScheduleSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TruckScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def truck_schedule_detail(request, slug):
    schedule = get_object_or_404(TruckSchedule, slug=slug)
    if request.method == "GET":
        serializer = TruckScheduleSerializer(schedule)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TruckScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def truck_route_list(request):
    if request.method == "GET":
        queryset = TruckRoute.objects.all()
        serializer = TruckRouteSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TruckRouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def truck_route_detail(request, slug):
    route = get_object_or_404(TruckRoute, slug=slug)
    if request.method == "GET":
        serializer = TruckRouteSerializer(route)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TruckRouteSerializer(route, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        route.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def truck_goods_list(request):
    if request.method == "GET":
        queryset = TruckGoods.objects.all()
        serializer = TruckGoodsSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TruckGoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def truck_goods_detail(request, slug):
    goods = get_object_or_404(TruckGoods, slug=slug)
    if request.method == "GET":
        serializer = TruckGoodsSerializer(goods)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TruckGoodsSerializer(goods, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        goods.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
