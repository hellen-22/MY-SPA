from django.db import models
from account.models import CustomUser

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='blog-title')
    content = models.TextField(verbose_name='blog-content')
    time_posted = models.DateTimeField()

    def __str__(self):
        return self.title