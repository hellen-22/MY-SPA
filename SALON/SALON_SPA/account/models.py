from django.db import models
from products.models import Service


class Appointment(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    time = models.TimeField()

    def __str__(self):
        return self.service
