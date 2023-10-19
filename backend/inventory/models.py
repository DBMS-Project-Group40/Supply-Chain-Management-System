# inventory/models.py

from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    train_capacity_consumption = models.PositiveIntegerField()

    class Meta:
        db_table = "product"


class TrainSchedule(models.Model):
    destination = models.CharField(max_length=100)  # Colombo, Negombo, etc.
    capacity = models.PositiveIntegerField()

    class Meta:
        db_table = "train_schedule"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    delivery_date = models.DateField()
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "order"
