from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from blog.models import Article
from serializers import CreateUserSerializer


# POST Method
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


def articles_list(request):
    articles = Article.objects.all()
    context = {'a': 4, 'articles': articles}
    return render(request, 'article/articles-list.html', context)


def article_details(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {
        "article": article,
    }
    return render(request, 'article/article-details.html', context)
