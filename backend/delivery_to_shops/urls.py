from django.urls import path
from . import views

urlpatterns = [
    path("shop-orders/", views.shop_order_list),
    path("shop-orders/<int:id>/", views.shop_order_detail),
    path("shop-deliveries/", views.shop_delivery_list),
    path("shop-deliveries/<slug:slug>/", views.shop_delivery_detail),
    path("truck-routes/", views.truck_route_list),
    path("truck-routes/<int:id>/", views.truck_route_detail),
    path("get-route-id/", views.get_route_id),
]
