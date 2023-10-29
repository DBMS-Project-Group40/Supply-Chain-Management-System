from django.urls import path
from . import views

urlpatterns = [
    path("users/all/", views.user_list),
    path("users/by_email/", views.get_user_by_email),
]
