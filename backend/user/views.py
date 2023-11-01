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
                "INSERT INTO users (ID, name, email, role, password) VALUES (%s, %s, %s, %s, %s)",
                [
                    request.data.get("ID"),
                    request.data.get("name"),
                    request.data.get("email"),
                    request.data.get("role"),
                    request.data.get("password"),
                ],
            )
        return HttpResponse(status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_by_email(request):
    email = request.GET.get("email", None)

    if email:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email = %s", [email])
            user = dictfetchall(cursor)

            if user:
                return JsonResponse(user[0], safe=False)
            else:
                return JsonResponse(
                    {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
                )
    else:
        return JsonResponse(
            {"error": "Email not provided"}, status=status.HTTP_400_BAD_REQUEST
        )
