from rest_framework import serializers
from .models import Source, SourceType

class SourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceType
        fields = ['id', 'name', 'source_type']

class SourceSerializer(serializers.ModelSerializer):
    type = SourceTypeSerializer()

    class Meta:
        model = Source
        fields = ['id', 'name', 'favicon', 'rss_feed_link', 'date_added', 'update_interval', 'type']

