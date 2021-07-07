from django.urls import path

from products.views import product_detail_view, product_create_view, product_delete_view, product_list_view

app_name = 'products'  # App name inside urls
urlpatterns = [path('<int:id>', product_detail_view, name='product-detail'),  # Dynamic routing
               path('create', product_create_view, name='product create'),
               path('<int:id>/delete', product_delete_view, name='Product delete'),
               path('list', product_list_view, name='list of objects'), ]