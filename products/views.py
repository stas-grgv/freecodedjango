from django.shortcuts import render

from .models import Product
from .forms import RawProductForm, ProductForm


# View with product detail. Now with id 1
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj,
    }
    return render(request, 'product/details.html', context)


# def product_create_view(request):
#     initial_data = {
#         "title": "Initial awesome title",
#     }
#     my_form = RawProductForm(initial=initial_data)
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             # Kwargs
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)
#
#     context = {"form": my_form}
#     return render(request, 'product/product-create.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "my_form": form
    }
    return render(request, 'product/product-create.html', context)
