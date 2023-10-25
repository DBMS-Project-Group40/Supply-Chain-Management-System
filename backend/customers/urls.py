from django.urls import path
from . import views


urlpatterns = [path("truck-routes/", views.truckroute_list)]
