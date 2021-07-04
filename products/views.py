from django.shortcuts import render

from .models import Product
from .forms import RawProductForm


# View with product detail. Now with id 1
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj,
    }
    return render(request, 'product/details.html', context)


def product_create_view(reqest):
    my_form = RawProductForm()
    if reqest.method == 'POST':
        my_form = RawProductForm(reqest.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            # Kwargs
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()
        else:
            print(my_form.errors)

    context = {"form": my_form}
    return render(reqest, 'product/product-create.html', context)
