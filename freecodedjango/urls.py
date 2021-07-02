from django.contrib import admin
from django.urls import path
from pages import views
from products.views import product_detail_view, product_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact page'),
    path('about', views.about_view, name='about view'),
    path('product/', product_detail_view, name='product'),
    path('new-product', product_create_view, name='product create')
]
