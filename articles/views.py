from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms
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


def new(request):
    # new_article = forms.ArticleForm()
    if request.method == "POST":
        new_article_form = forms.ArticleForm(request.POST)
        message = '请检查填写的内容'
        if new_article_form.is_valid():
            title = new_article_form.cleaned_data.get('title')
            text = new_article_form.cleaned_data.get('text')
            print('title==%s, text=%s' % (title, text))
            same_title = models.Article.objects.filter(title=title)
            if same_title == title:
                message = '标题已经存在'
                return render(request, 'articles/new.html', locals())
            new_article = models.Article()
            new_article.title = title
            new_article.text = text
            new_article.save()
            return redirect('/articles/index/')
        # return redirect(request, 'articles/new.html', locals())
        return redirect('/articles/index/')
    new_article_form = forms.ArticleForm()
    return render(request, 'articles/new.html', locals())


def edit(request, article_id):
    article = get_object_or_404(models.Article, id=article_id)
    # article_to_edit = forms.ArticleForm(locals())
    return render(request, 'articles/edit.html', locals())

