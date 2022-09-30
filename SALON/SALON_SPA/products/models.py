from django.db import models
from django.conf import settings

class Categories(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category


class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20, verbose_name='name')
    description = models.TextField(max_length=200, verbose_name='description')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('C', 'Completed'),
        ('P', 'Pending'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=255, choices=PAYMENT_CHOICES)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


    def __str__(self) -> str:
        return str(self.customer)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.order)







