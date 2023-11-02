from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:id>/", views.product_detail),
    path("products-count/", views.product_count),
    path("categories/", views.num_of_product_categories),
    path("train-schedules/", views.train_schedule_list),
    path("train-schedules/<int:id>/", views.train_schedule_detail),
    path("orders/", views.order_list),
    path("orders/<int:id>/", views.order_detail),
    path("bills/", views.bill_list),
    path("bills/<int:id>/", views.bill_detail),
    path("bill-entries/", views.add_bill_entry),
    path(
        "orders/customer/<int:customer_id>/",
        views.get_orders_by_customer,
    ),
]
