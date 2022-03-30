from django.db import models
from account.models import *

class Product(models.Model):
    image = models.ImageField
    name = models.CharField(max_length=20, verbose_name='name')
    description = models.TextField(max_length=200, verbose_name='description')
    category = models.CharField(max_length=50)
    price = models.IntegerField(verbose_name='price')
    rating = models.IntegerField()

    def ___str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.IntegerField(verbose_name='service_price')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_method = models.CharField(max_length=50, null=True)
    payment_id = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s" % (self.user)