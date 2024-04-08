from .models import Article
import django_filters
import django_filters as filters

class ArticleFilter(django_filters.FilterSet):
    datetime_from = django_filters.DateTimeFilter(field_name='datetime', lookup_expr='gte')
    datetime_to = django_filters.DateTimeFilter(field_name='datetime', lookup_expr='lte')
    title = django_filters.CharFilter(lookup_expr='icontains')
    source__name = django_filters.CharFilter(field_name='source__name', lookup_expr='icontains')
    keywords = django_filters.CharFilter(lookup_expr='icontains')
    source__id = filters.UUIDFilter(field_name='source__id')
    source__type__name = filters.CharFilter(field_name='source__type__name', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'source__name', 'source__id', 'source__type__name', 'keywords', 'datetime_from', 'datetime_to']
