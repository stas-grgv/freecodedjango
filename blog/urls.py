from django.urls import path
from blog.views import articles_list, article_details

app_name = 'blog'
urlpatterns = [
    path('', articles_list, name='articles list'),
    path('<int:id>', article_details, name='article details')
]
