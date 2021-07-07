from django.contrib import admin
from django.urls import path, include

import products.urls
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact page'),
    path('about', views.about_view, name='about view'),
    path('products/', include(products.urls))
]
