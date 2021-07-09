from django.contrib import admin
from django.urls import path, include

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
