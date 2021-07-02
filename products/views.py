from django.shortcuts import render

from .models import Product
from .forms import ProductForm


# View with product detail. Now with id 1
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "price":obj.price,
    # }
    context = {
        'object': obj,
    }
    return render(request, 'product/details.html', context)


# View with create product form
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/product-create.html", context)
