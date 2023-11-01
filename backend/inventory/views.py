from django.http import JsonResponse, HttpResponse
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework import status


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM product")
            products = dictfetchall(cursor)
        return JsonResponse(products, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO product (name, description) VALUES (%s, %s)",
                [request.data.get("name"), request.data.get("description")],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, id):
    with connection.cursor() as cursor:
        if request.method == "GET":
            cursor.execute("SELECT * FROM product WHERE id = %s", [id])
            product = cursor.fetchone()
            if product:
                return JsonResponse(
                    dict(zip([col[0] for col in cursor.description], product))
                )
            else:
                return HttpResponse(status=404)
        elif request.method == "PUT":
            cursor.execute(
                "UPDATE product SET name = %s, description = %s WHERE id = %s",
                [request.data.get("name"), request.data.get("description"), id],
            )
            return HttpResponse(status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            cursor.execute("DELETE FROM product WHERE id = %s", [id])
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def product_count(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM product")
            count = cursor.fetchone()[0]
        return JsonResponse({"count": count})


@api_view(["GET"])
def num_of_product_categories(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(DISTINCT product_name) FROM product")
            distinct_categories = cursor.fetchone()[0]
        return JsonResponse({"categories": distinct_categories})


@api_view(["GET", "POST"])
def train_schedule_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM trainschedule")
            schedules = dictfetchall(cursor)
        return JsonResponse(schedules, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            # Assuming TrainSchedule has fields like 'train_name', 'departure', 'arrival'
            cursor.execute(
                "INSERT INTO yourapp_trainschedule (train_name, departure, arrival) VALUES (%s, %s, %s)",
                [
                    request.data.get("train_name"),
                    request.data.get("departure"),
                    request.data.get("arrival"),
                ],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def train_schedule_detail(request, id):
    with connection.cursor() as cursor:
        if request.method == "GET":
            cursor.execute("SELECT * FROM yourapp_trainschedule WHERE id = %s", [id])
            schedule = cursor.fetchone()
            if schedule:
                return JsonResponse(
                    dict(zip([col[0] for col in cursor.description], schedule))
                )
            else:
                return HttpResponse(status=404)
        elif request.method == "PUT":
            cursor.execute(
                "UPDATE yourapp_trainschedule SET train_name = %s, departure = %s, arrival = %s WHERE id = %s",
                [
                    request.data.get("train_name"),
                    request.data.get("departure"),
                    request.data.get("arrival"),
                    id,
                ],
            )
            return HttpResponse(status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            cursor.execute("DELETE FROM yourapp_trainschedule WHERE id = %s", [id])
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def order_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM order")
            orders = dictfetchall(cursor)
        return JsonResponse(orders, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            # Assuming Order has fields like 'product_id', 'quantity'
            cursor.execute(
                "INSERT INTO order (OrderID, BillID, CustomerID, RouteID) VALUES (%s, %s, %s, %s)",
                [request.data.get("product_id"), request.data.get("quantity")],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def order_detail(request, id):
    with connection.cursor() as cursor:
        if request.method == "GET":
            cursor.execute("SELECT * FROM order WHERE id = %s", [id])
            order = cursor.fetchone()
            if order:
                return JsonResponse(
                    dict(zip([col[0] for col in cursor.description], order))
                )
            else:
                return HttpResponse(status=404)
        elif request.method == "PUT":
            cursor.execute(
                "UPDATE yourapp_order SET product_id = %s, quantity = %s WHERE id = %s",
                [request.data.get("product_id"), request.data.get("quantity"), id],
            )
            return HttpResponse(status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            cursor.execute("DELETE FROM yourapp_order WHERE id = %s", [id])
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def bill_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM yourapp_bill")
            bills = dictfetchall(cursor)
        return JsonResponse(bills, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            # Assuming Bill has fields like 'order_id', 'amount'
            cursor.execute(
                "INSERT INTO yourapp_bill (order_id, amount) VALUES (%s, %s)",
                [request.data.get("order_id"), request.data.get("amount")],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def bill_detail(request, id):
    with connection.cursor() as cursor:
        if request.method == "GET":
            cursor.execute("SELECT * FROM yourapp_bill WHERE id = %s", [id])
            bill = cursor.fetchone()
            if bill:
                return JsonResponse(
                    dict(zip([col[0] for col in cursor.description], bill))
                )
            else:
                return HttpResponse(status=404)
        elif request.method == "PUT":
            cursor.execute(
                "UPDATE yourapp_bill SET order_id = %s, amount = %s WHERE id = %s",
                [request.data.get("order_id"), request.data.get("amount"), id],
            )
            return HttpResponse(status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            cursor.execute("DELETE FROM yourapp_bill WHERE id = %s", [id])
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
