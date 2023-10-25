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


class TruckSchedule(models.Model):
    truck = models.ForeignKey("Truck", on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    slug = models.SlugField()


class TruckGoods(models.Model):
    route = models.ForeignKey("TruckRoute", on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    slug = models.SlugField()


class TruckRoute(models.Model):
    schedule = models.ForeignKey(TruckSchedule, on_delete=models.CASCADE)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)
    slug = models.SlugField()
