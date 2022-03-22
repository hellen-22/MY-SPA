from django.db import models

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
