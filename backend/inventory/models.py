from django.db import models


class Product(models.Model):
    ProductID = models.CharField(max_length=7, primary_key=True)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_count = models.IntegerField()

    class Meta:
        db_table = "product"


class TrainSchedule(models.Model):
    train_schedule_id = models.CharField(max_length=7, primary_key=True)
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


class Bill(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    total_list_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "bill"
