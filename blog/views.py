from django.shortcuts import render



def home(request):

    return render(request, 'index.html')


def article(request):

    return render(request, 'article.html')
