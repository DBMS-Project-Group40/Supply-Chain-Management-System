from django.urls import path
from . import views

urlpatterns = [
    path("shop-orders/", views.shop_order_list),
    path("shop-orders/<int:id>/", views.shop_order_detail),
    path("shop-deliveries/", views.shop_delivery_list),
    path("shop-deliveries/<int:id>/", views.shop_delivery_detail),
    path("trucks/", views.truck_list),
    path("trucks/<int:id>/", views.truck_detail),
    path("truck-schedules/", views.truck_schedule_list),
    path("truck-schedules/<int:id>/", views.truck_schedule_detail),
    path("truck-routes/", views.truck_route_list),
    path("truck-routes/<int:id>/", views.truck_route_detail),
    path("truck-goods/", views.truck_goods_list),
    path("truck-goods/<int:id>/", views.truck_goods_detail),
]
