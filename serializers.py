from django.contrib.auth.models import User, Group
from rest_framework import serializers

from products.models import Order, Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'id']
