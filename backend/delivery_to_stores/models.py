from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    slug = models.SlugField()


class Truck(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    slug = models.SlugField()
