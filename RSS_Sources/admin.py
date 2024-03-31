from django.contrib import admin
from .models import *

class SourceTable(admin.ModelAdmin):
    list_display = ("name", "type", "date_added", "rss_feed_link")

class SourceTypeTable(admin.ModelAdmin):
    list_display = ("name", "source_type")

# Register your models here.
admin.site.register(SourceType, SourceTypeTable)
admin.site.register(Source, SourceTable)
admin.site.register(RSS_Cache)