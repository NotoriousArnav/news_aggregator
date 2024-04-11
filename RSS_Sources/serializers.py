from rest_framework import serializers
from .models import Source, SourceType
from datetime import date

class SourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceType
        fields = ['id', 'name', 'source_type']

class SourceSerializer(serializers.ModelSerializer):
    type = SourceTypeSerializer()
    article_count = serializers.SerializerMethodField()

    def get_article_count(self, obj):
        return obj.article_set.filter(datetime__date=date.today()).count()

    class Meta:
        model = Source
        fields = ['id', 'name', 'favicon', 'rss_feed_link', 'date_added', 'update_interval', 'type', 'article_count']

