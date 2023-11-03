from datetime import date
from django.http import JsonResponse, HttpResponse
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework import status


def convert_query_result_to_dict_list(cursor, query_result):
    """
    Converts a query result into a list of dictionaries
    where keys are the column names and values are row values.
    """
    return [
        dict(zip([col[0] for col in cursor.description], row)) for row in query_result
    ]


@api_view(["GET"])
def get_transport_managers(request):
    raw_query = """
    SELECT
        CONCAT(u.first_name, " ", u.last_name ) AS name,
        m.salary
    FROM TransportManager m
    JOIN User u ON u.ID = m.ManagerID
    """
    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        query_result = cursor.fetchall()
        result = convert_query_result_to_dict_list(cursor, query_result)

    return JsonResponse(result, safe=False, status=status.HTTP_200_OK)
