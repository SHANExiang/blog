from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('', views.dashboard)
]