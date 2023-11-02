from django.urls import path
from . import views

urlpatterns = [
    path("get-store-and-end-location/", views.get_store_and_end_location),
    path("train-goods/", views.get_train_goods),
]
