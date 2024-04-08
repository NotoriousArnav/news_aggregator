from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .filters import ArticleFilter
from .serializers import ArticleSerializer

class ArticleListAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter
