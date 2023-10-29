from django.http import JsonResponse, HttpResponse
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = dictfetchall(cursor)
        return JsonResponse(users, safe=False)
    elif request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (name, email, role, password) VALUES (%s, %s, %s, %s)",
                [
                    request.data.get("name"),
                    request.data.get("email"),
                    request.data.get("role"),
                    request.data.get("password"),
                ],
            )
        return HttpResponse(status=status.HTTP_200_OK)
