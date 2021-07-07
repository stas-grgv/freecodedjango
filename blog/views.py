from django.shortcuts import render


# Create your views here.
from blog.models import Article


def articles_list(request):
    articles = Article.objects.all()
    context = {'a': 4, 'articles': articles}
    return render(request, 'article/articles-list.html', context)
