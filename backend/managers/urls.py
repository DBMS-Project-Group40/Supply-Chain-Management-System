from django.urls import path
from .views import get_transport_managers

urlpatterns = [
    path("transport-managers/", get_transport_managers, name="transport-managers"),
]
