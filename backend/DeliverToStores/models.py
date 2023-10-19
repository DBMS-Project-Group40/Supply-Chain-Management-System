from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)


class Truck(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()


class TruckSchedule(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class TruckRoute(models.Model):
    schedule = models.ForeignKey(TruckSchedule, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class TruckGoods(models.Model):
    route = models.ForeignKey(TruckRoute, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
