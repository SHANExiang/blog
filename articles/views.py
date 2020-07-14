from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    classifications = models.Classification.objects.all()
    return render(request, 'articles/index.html', locals())


def dashboard(request):
    total = models.Article.objects.count()
    classifications = models.Classification.objects.all()
    classifications_list = list()
    rates_list = list()
    for classification in classifications:
        classification_articles = models.Article.objects.filter(
            classification=classification).count()
        classifications_list.append(
            {'%s' % classification: classification_articles})
        classification_rate = round(classification_articles / total * 100)
        rates_list.append({'%s' % classification: classification_rate})
    return render(request, 'articles/dashboard.html', locals())


def detail(request, article_id):
    article = get_object_or_404(models.Article, id=article_id)
    return render(request, 'articles/detail.html', locals())