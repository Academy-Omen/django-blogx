from django.shortcuts import render


def home(request):

    return render(request, 'index.html')


def articles(request):

    return render(request, 'articles.html')


def article(request):

    return render(request, 'article.html')
