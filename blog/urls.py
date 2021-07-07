from django.urls import path
from blog.views import articles_list

app_name = 'blog'
urlpatterns = [
    path('', articles_list, name='articles list'),
]
