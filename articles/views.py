from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    classifications = models.Classification.objects.all()
    return render(request, 'articles/index.html', locals())


def dashboard(request):
    pass
    return render(request, 'articles/dashboard.html', locals())


def detail(request, article_id):
    article = get_object_or_404(models.Article, id=article_id)
    return render(request, 'articles/detail.html', locals())