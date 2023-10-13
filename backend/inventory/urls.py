from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("bills/", views.bill_list),
    path("products/<int:id>/", views.product_detail),
]
