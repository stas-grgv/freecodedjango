from django.urls import path, include
from rest_framework import routers
from products import views

from products.views import product_detail_view, product_create_view, product_delete_view, product_list_view

app_name = 'products'  # App name inside urls
router = routers.DefaultRouter()
router.register(r'all', views.ProductViewSet)  # All products view set
router.register(r'orders', views.OrdersViewSet)

urlpatterns = [path('<int:id>', product_detail_view, name='product-detail'),  # Dynamic routing
               path('create', product_create_view, name='product create'),
               path('<int:id>/delete', product_delete_view, name='Product delete'),
               path('list', product_list_view, name='list of objects'),
               path('api/', include(router.urls)),
               path('orders/', include(router.urls)),
               ]
