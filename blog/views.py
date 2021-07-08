from django.http import Http404
from django.shortcuts import render

# Create your views here.
from blog.models import Article


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
