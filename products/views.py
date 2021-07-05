from django.shortcuts import render

from .models import Product
from .forms import RawProductForm, ProductForm


# View with product detail. Now with id 1
def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
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
