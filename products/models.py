from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
import datetime


class Product(models.Model):
    title = models.CharField("Название продукта", max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=False)

    # Выводить title модели вместо Product etc..
    def __str__(self):
        return self.title

    # Dynamic url with id argument
    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})


class Client(models.Model):
    name = models.CharField(max_length=160)

    def __str__(self):
        return self.name


class Order(models.Model):
    address = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)

    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.client.name}: Создан:{self.date_created}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=CASCADE, blank=True, editable=True, null=True)
    quantity = models.IntegerField(default=0, blank=False, editable=True)
    order = models.ForeignKey(Order, blank=True, null=True, editable=True, on_delete=CASCADE)
