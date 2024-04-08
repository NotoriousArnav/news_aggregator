
from rest_framework import serializers
from RSS_Sources.models import Source, SourceType
from RSS_Sources.serializers import SourceSerializer, SourceTypeSerializer
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    source = SourceSerializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'source', 'description', 'content', 'link', 'thumbnail', 'datetime', 'keywords', 'md5hash_value']
