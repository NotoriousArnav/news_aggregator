from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .filters import ArticleFilter
from .serializers import ArticleSerializer
from django.db.models import Count

class ArticleListAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.annotate(
        num_duplicates=Count('md5hash_value')
    ).filter(
        num_duplicates=1,
        link__in=Article.objects.values('link').annotate(
            link_count=Count('link')
        ).filter(
            link_count=1
        ).values_list('link', flat=True)
    ).order_by('-datetime')
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter
