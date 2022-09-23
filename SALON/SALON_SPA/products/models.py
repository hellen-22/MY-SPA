from statistics import mode
from django.db import models
from account.models import *
from datetime import datetime

class Categories(models.Model):
    category = models.CharField(max_length=255)


class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20, verbose_name='name')
    description = models.TextField(max_length=200, verbose_name='description')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='price')
    rating = models.IntegerField()

    def __str__(self):
        return str(self.category)

class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.IntegerField(verbose_name='service_price')

    def __str__(self):
        return self.name
