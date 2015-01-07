# Django Modules
from django.shortcuts import render

# App Modules
from .models import Article


def index(request):
    """Index view"""
    context = {}
    return render(request, 'cms/index.html', context)
