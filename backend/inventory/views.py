from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, TrainSchedule, Order, Bill
from .serializers import (
    ProductSerializer,
    TrainScheduleSerializer,
    OrderSerializer,
    BillSerializer,
)


@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        queryset = Product.objects.all()
        serializer = ProductSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "GET":
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def train_schedule_list(request):
    if request.method == "GET":
        queryset = TrainSchedule.objects.all()
        serializer = TrainScheduleSerializer(queryset, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = TrainScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def train_schedule_detail(request, id):
    train_schedule = get_object_or_404(TrainSchedule, pk=id)
    if request.method == "GET":
        serializer = TrainScheduleSerializer(train_schedule)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TrainScheduleSerializer(train_schedule, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        train_schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def order_list(request):
    if request.method == "GET":
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def order_detail(request, id):
    order = get_object_or_404(Order, pk=id)
    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = OrderSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def bill_list(request):
    if request.method == "GET":
        queryset = Bill.objects.all()
        serializer = BillSerializer(queryset, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def bill_detail(request, id):
    bill = get_object_or_404(Bill, pk=id)
    if request.method == "GET":
        serializer = BillSerializer(bill)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BillSerializer(bill, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
