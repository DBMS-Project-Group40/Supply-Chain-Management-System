from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db import connection


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


@api_view(["GET"])
def get_store_and_end_location(request):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT
                s.StoreID AS StoreID,
                tg.end_location AS end_location
            FROM
                Store AS s
            INNER JOIN
                TrainSchedule AS ts ON s.StoreID = ts.StoreID
            INNER JOIN
                TrainGoods AS tg ON ts.train_schedule_id = tg.train_schedule_id
        """
        )
        result = dictfetchall(cursor)

    return JsonResponse(result, safe=False)


# GET train goods data
@api_view(["GET"])
def get_train_goods(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    tg.OrderID AS OrderID,
                    tg.train_schedule_id AS train_schedule_id,
                    tg.sending_qty AS sending_qty,
                    tg.end_location AS end_location
                FROM
                    TrainGoods AS tg
                """
            )
            result = dictfetchall(cursor)

        return JsonResponse(result, safe=False)
