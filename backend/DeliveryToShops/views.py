from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ShopOrder, ShopDelivery
from .serializations import ShopOrderSerializer, ShopDeliverySerializer


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
def shop_order_detail(request, slug):
    order = get_object_or_404(ShopOrder, slug=slug)
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
