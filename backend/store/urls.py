from django.urls import path
from . import views


urlpatterns = [path("products/", views.product_list), path("bills/", views.bills_list)]
