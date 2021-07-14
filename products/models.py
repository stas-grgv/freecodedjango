from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)
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


class OrderItem(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=0, blank=False, editable=True)


class Order(models.Model):
    items = models.ManyToManyField(OrderItem)
    address = models.TextField()
    client_name = models.CharField(max_length=120)
