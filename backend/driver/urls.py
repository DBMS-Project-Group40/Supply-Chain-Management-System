from django.urls import path
from .views import get_assigned_route_for_driver, get_all_drivers

urlpatterns = [
    path("driver-routes/<int:driver_id>/", get_assigned_route_for_driver),
    path("drivers/", get_all_drivers),
    # other paths...
]
