from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('edit/<int:article_id>', views.edit, name='edit'),
    path('new/', views.new, name='new'),
    path('', views.dashboard)
]