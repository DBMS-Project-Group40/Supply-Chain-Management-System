from django.urls import path
from . import views

urlpatterns = [
    path("stores/", views.store_list),
    path("stores/<slug:slug>/", views.store_detail),
    path("trucks/", views.truck_list),
    path("trucks/<slug:slug>/", views.truck_detail),
    path("truck-schedules/", views.truck_schedule_list),
    path("truck-schedules/<slug:slug>/", views.truck_schedule_detail),
    path("truck-goods/", views.truck_goods_list),
    path("truck-goods/<slug:slug>/", views.truck_goods_detail),
]
