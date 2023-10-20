from django.db import models


class ShopOrder(models.Model):
    store = models.ForeignKey("delivery_to_stores.Store", on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    slug = models.SlugField()

    class Meta:
        db_table = "shoporder"


class ShopDelivery(models.Model):
    order = models.ForeignKey(ShopOrder, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()
    slug = models.SlugField()
