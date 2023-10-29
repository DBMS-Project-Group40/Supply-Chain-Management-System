from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ShopOrder, ShopDelivery, TruckRoute
from .serializations import (
    ShopOrderSerializer,
    ShopDeliverySerializer,
    TruckRouteSerializer,
)
from django.db import connection
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


@api_view(["GET", "POST"])
def shop_order_list(request):
    if request.method == "GET":
        queryset = ShopOrder.objects.all()
        serializer = ShopOrderSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ShopOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def shop_order_detail(request, id):
    order = get_object_or_404(ShopOrder, pk=id)
    if request.method == "GET":
        serializer = ShopOrderSerializer(order)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ShopOrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def shop_delivery_list(request):
    if request.method == "GET":
        queryset = ShopDelivery.objects.all()
        serializer = ShopDeliverySerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ShopDeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def shop_delivery_detail(request, slug):
    delivery = get_object_or_404(ShopDelivery, slug=slug)
    if request.method == "GET":
        serializer = ShopDeliverySerializer(delivery)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ShopDeliverySerializer(delivery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def truck_route_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM truckroute")
            routes = dictfetchall(cursor)
        return JsonResponse(routes, safe=False)

    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO truckroute (RouteID, City, start_location, end_location, Duration) VALUES (%s, %s, %s, %s, %s)",
                [
                    request.data.get("RouteID"),
                    request.data.get("City"),
                    request.data.get("start_location"),
                    request.data.get("end_location"),
                    request.data.get("Duration"),
                ],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_route_id(request):
    if request.method == "GET":
        start_location = request.query_params.get("start_location")
        end_location = request.query_params.get("end_location")

        if not start_location or not end_location:
            return JsonResponse(
                {"error": "Both start_location and end_location are required."},
                status=400,
            )

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT RouteID FROM truckroute WHERE start_location = %s AND end_location = %s",
                [start_location, end_location],
            )
            row = cursor.fetchone()
            if row:
                route_id = row[0]
                return JsonResponse({"RouteID": route_id})
            else:
                return JsonResponse({"error": "Route not found."}, status=404)


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
