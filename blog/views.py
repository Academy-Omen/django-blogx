from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Profile, Tag, Article
from django.views.generic import ListView


def home(request):

    # feature articles on the home page
    featured = Article.articlemanager.filter(featured=True)[0:3]

    context = {
        'articles': featured
    }

    return render(request, 'index.html', context)


def articles(request, tag = None):
    
    
    

    # all articles on the home page
    articles = Article.articlemanager.all()

    # filtering by category
    if tag:
        articles = Article.articlemanager.filter(tags=tag)

    tags = Tag.objects.all()

    context = {
        'articles': articles,
        'tags': tags,
    }

    return render(request, 'articles.html', context)


def article(request):

    return render(request, 'article.html')
