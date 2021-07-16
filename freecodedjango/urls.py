from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Custom imports
import pages.urls
import products.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(pages.urls)),
    path('products/', include(products.urls)),
]
