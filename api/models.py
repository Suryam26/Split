from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Bill(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=256)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    bill = models.ForeignKey(
        Bill, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Consumer(models.Model):
    name = models.CharField(max_length=256)
    bill = models.ForeignKey(
        Bill, related_name='consumers', on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='consumers')

    def __str__(self):
        return self.name
