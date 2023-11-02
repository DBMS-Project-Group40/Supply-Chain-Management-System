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
def get_assigned_route_for_driver(request, driver_id):
    with connection.cursor() as cursor:
        if request.method == "GET":
            # Set the current date
            current_date = date.today()

            # SQL query to get the details of the assigned TruckRoute for the specified driver
            query = """
            SELECT TR.RouteID, TR.City, TR.start_location, TR.end_location, TS.time_to_leave, TR.Duration
            FROM TruckSchedule AS TS
            JOIN TruckRoute AS TR ON TS.RouteID = TR.RouteID
            WHERE TS.DriverID = %s AND TS.schedule_date = %s;
            """

            # Execute the query with the provided driver_id and current_date as parameters
            cursor.execute(query, [driver_id, current_date])

            # Fetch the results
            routes = cursor.fetchall()

            if routes:
                routes_list = convert_query_result_to_dict_list(
                    cursor, routes
                )  # pass routes as the second argument
                return JsonResponse(routes_list, safe=False)
            else:
                return HttpResponse(status=404)  # Not Found
        else:
            return HttpResponse(status=405)  # Method Not Allowed


@api_view(["GET"])
def get_all_drivers(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            # Query to select all drivers from the Driver table
            cursor.execute("SELECT * FROM Driver")

            # Fetch the results
            drivers = cursor.fetchall()

            if drivers:
                drivers_list = convert_query_result_to_dict_list(cursor, drivers)
                return JsonResponse(drivers_list, safe=False)
            else:
                return HttpResponse(status=404)  # Not Found (if there are no drivers)
    else:
        return HttpResponse(status=405)  # Method Not Allowed
