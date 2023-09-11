from django.urls import path
from .views import ArticleListView, ArticleRateView

urlpatterns = [
    path("articles/",ArticleListView.as_view(),name = 'articles'),
    path("artiles_rate/", ArticleRateView.as_view(), name = "article_rate")
]
