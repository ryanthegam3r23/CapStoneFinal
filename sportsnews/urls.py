from django.urls import path
from . import views

app_name = 'sportsnews'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<int:pk>/', views.article_detail, name='detail'),
    path('<int:pk>/like/', views.like_article, name='like_article'),  # if exists
]


