from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    bill = models.ForeignKey("Bill", on_delete=models.RESTRICT)

    class Meta:
        db_table = "products"


class Bill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    total_list_price = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = "Bills"
