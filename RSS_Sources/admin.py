from django.contrib import admin
from .models import *

class SourceTable(admin.ModelAdmin):
    list_display = ("name", "type", "typetype", "date_added", "rss_feed_link", "updates", "last_updated")

    def updates(self, cls):
        return cls.rss_cache_set.count()

    def typetype(self, cls):
        return cls.type.source_type

    def last_updated(self, cls):
        try:
            val = cls.rss_cache_set.all()[0].timestamp
        except:
            val = None
        return val

class SourceTypeTable(admin.ModelAdmin):
    list_display = ("name", "get_sources", "source_type")

    def get_sources(self, cls):
        return cls.source_set.count()

class RSSCache(admin.ModelAdmin):
    list_display = ("source", "timestamp", "cache_value")

    def cache_value(self, cls):
        return '...'+cls.cache[20:120]+'...'

# Register your models here.
admin.site.register(SourceType, SourceTypeTable)
admin.site.register(Source, SourceTable)
admin.site.register(RSS_Cache, RSSCache)