from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, response
from rest_framework import generics, serializers, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from serializers import OrderSerializer, ProductSerializer, CreateUserSerializer, OrderItemSerializer
from .models import Order, Product, OrderItem
from .forms import RawProductForm, ProductForm


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = permissions.IsAuthenticated


# View with product detail. Now with id 1
def product_detail_view(request, id):
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    if obj:
        context = {
            'object': obj,
        }
    return render(request, 'product/details.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "my_form": form
    }
    return render(request, 'product/product-create.html', context)


def product_delete_view(request, id):
    form = ProductForm(request.POST or None)
    obj = Product.objects.get(id=id)
    print(obj.title)
    if request.method == 'POST':
        obj.delete()
        return redirect('/')

    context = {
        "form": form,
        "product": obj,
    }
    return render(request, 'product/product-delete.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset,
    }

    return render(request, 'product/product-list.html', context)
