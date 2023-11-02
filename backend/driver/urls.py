from django.urls import path
from . import views

urlpatterns = [
    path("driver/<int:driver_id>/routes/", views.get_assigned_route_for_driver),
]
