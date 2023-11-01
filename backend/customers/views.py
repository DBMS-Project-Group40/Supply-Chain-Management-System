from django.db import connection
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


@api_view(["GET", "POST"])
def truckroute_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM TruckRoute")
            routes = dictfetchall(cursor)
        return JsonResponse(routes, safe=False)

    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO TruckRoute (RouteID, City, start_location, end_location, Duration) VALUES (%s, %s, %s, %s, %s)",
                [
                    request.data.get("RouteID"),
                    request.data.get("City"),
                    request.data.get("start_location"),
                    request.data.get("end_location"),
                    request.data.get("Duration"),
                ],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def customer_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Customer")
            customers = dictfetchall(cursor)
        return JsonResponse(customers, safe=False)

    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Customer (CustomerID, points, address, city) VALUES (%s, %s, %s, %s)",
                [
                    request.data.get("CustomerID"),
                    request.data.get("points"),
                    request.data.get("address"),
                    request.data.get("City"),
                ],
            )
        return HttpResponse(status=status.HTTP_201_CREATED)
