from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock_count = models.IntegerField()
