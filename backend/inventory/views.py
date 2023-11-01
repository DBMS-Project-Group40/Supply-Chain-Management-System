from django.http import JsonResponse, HttpResponse
from django.db import connection, IntegrityError
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
            cursor.execute("SELECT * FROM Product")
            products = dictfetchall(cursor)
        return JsonResponse(products, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Product (product_name, price, stock_count) VALUES (%s, %s, %s)",
                [
                    request.data.get("product_name"),
                    request.data.get("price"),
                    request.data.get("stock_count"),
                ],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_product_by_id(request, product_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Product WHERE ProductID = %s", [product_id])
        product = dictfetchall(cursor)

    if product:
        return JsonResponse(product[0])
    else:
        return HttpResponse("Product not found", status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, id):
    with connection.cursor() as cursor:
        if request.method == "GET":
            cursor.execute("SELECT * FROM Product WHERE ProductID = %s", [id])
            product = cursor.fetchone()
            if product:
                return JsonResponse(
                    dict(zip([col[0] for col in cursor.description], product))
                )
            else:
                return HttpResponse(status=404)
        elif request.method == "PUT":
            cursor.execute(
                "UPDATE Product SET product_name = %s, price = %s, stock_count = %s WHERE ProductID = %s",
                [
                    request.data.get("product_name"),
                    request.data.get("price"),
                    request.data.get("stock_count"),
                    ProductID,
                ],
            )
            return HttpResponse(status=status.HTTP_200_OK)
        elif request.method == "DELETE":
            cursor.execute("DELETE FROM Product WHERE ProductID = %s", [ProductID])
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def product_count(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM Product")
            count = cursor.fetchone()[0]
        return JsonResponse({"count": count})


@api_view(["GET"])
def num_of_product_categories(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(DISTINCT product_name) FROM Product")
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
            cursor.execute("SELECT * FROM `Order`")
            orders = dictfetchall(cursor)
        return JsonResponse(orders, safe=False)
    elif request.method == "POST":
        bill_id = request.data.get("BillID")
        customer_id = request.data.get("CustomerID")
        route_id = request.data.get("RouteID")

        # Validate the received data before processing
        if not all([bill_id, customer_id, route_id]):
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO `Order` (BillID, CustomerID, RouteID) VALUES (%s, %s, %s)",
                    [bill_id, customer_id, route_id],
                )
            except IntegrityError:
                # Handle the case where there's a conflict or other database error
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        return HttpResponse(
            status=status.HTTP_201_CREATED
        )  # Return 201 for successful creation


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
            cursor.execute("SELECT * FROM Bill")
            bills = dictfetchall(cursor)
        return JsonResponse(bills, safe=False)

    elif request.method == "POST":
        # Retrieve the new fields from the request data
        bill_date = request.data.get("BillDate")
        total_list_price = request.data.get("total_list_price")
        discount_percent = request.data.get("discount_percent")
        total_discounted_price = request.data.get("total_discounted_price")

        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    """
                    INSERT INTO Bill (BillDate, total_list_price, discount_percent, total_discounted_price)
                    VALUES (%s, %s, %s, %s)
                    """,
                    [
                        bill_date,
                        total_list_price,
                        discount_percent,
                        total_discounted_price,
                    ],
                )
                # Get the ID of the newly created bill
                new_bill_id = cursor.lastrowid

            except IntegrityError as e:
                # Handle database errors here (like unique constraint failures)
                return JsonResponse(
                    {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
                )

        return JsonResponse(
            {"success": "Bill created successfully.", "BillID": new_bill_id}
        )


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


@api_view(["GET", "POST"])
def add_bill_entry(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            try:
                cursor.execute("SELECT * FROM `BillEntry`")
                bill_entries = dictfetchall(cursor)
            except Exception as e:
                return JsonResponse(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            return JsonResponse(bill_entries, safe=False)

    elif request.method == "POST":
        bill_id = request.data.get("BillID")
        product_id = request.data.get("ProductID")
        quantity = request.data.get("quantity")

        # Detailed checks for each field
        if not bill_id:
            return JsonResponse(
                {"error": "BillID is missing or invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not product_id:
            return JsonResponse(
                {"error": "ProductID is missing or invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not quantity:
            return JsonResponse(
                {"error": "Quantity is missing or invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with connection.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO `BillEntry` (BillID, ProductID, quantity) VALUES (%s, %s, %s)",
                    [bill_id, product_id, quantity],
                )
            except Exception as e:
                return JsonResponse(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return JsonResponse({"success": "Bill entry created successfully."})
