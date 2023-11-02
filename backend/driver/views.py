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
def get_assigned_route_for_driver(request, driver_id):
    with connection.cursor() as cursor:
        if request.method == "GET":
            # Call the stored procedure with the driver_id as a parameter
            cursor.callproc("GetAssignedRouteForDriver", [driver_id])

            # Fetch the results.
            routes = cursor.fetchall()

            if routes:
                routes_list = convert_query_result_to_dict_list(cursor, routes)
                return JsonResponse(routes_list, safe=False)
            else:
                return HttpResponse(status=404)
        else:
            return HttpResponse(status=405)  # Method Not Allowed
