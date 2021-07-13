from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views as v

# Custom imports
import pages.urls
import products.urls
import blog.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(pages.urls)),
    path('products/', include(products.urls)),
    path('blog/', include(blog.urls)),
]
