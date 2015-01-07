# Django Modules
from django.shortcuts import render

# App Modules
from .models import Article


def index(request):
    """Index view"""
    context = {}
    return render(request, 'cms/index.html', context)


def article(request, slug):
    context = {}
    context['article'] = Article.objects.filter(slug=slug)
    return render(request, 'cms/article.html', context)
