from django.db import models


# Create your models here.
# class Order(models.Model):
#     # order_id = models.CharField(primary_key=True, max_length=7)
#     bill_id = models.ForeignKey("Bill", on_delete=models.CASCADE)


# class Bill(models.Model):
#     # bill_id = models.CharField(primary_key=True, max_length=7)
#     # id = models.ForeignKey("Product", on_delete=models.RESTRICT)
#     total_list_price = models.DecimalField(max_digits=8, decimal_places=2)
#     discount_percent = models.xIntegerField()


class Product(models.Model):
    # id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
