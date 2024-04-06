from django.contrib import admin
from .models import *

class ArticleTable(admin.ModelAdmin):
    list_display = ["source", "sourceType", "title", "description", "keywords", "md5hash_value", "datetime"]

    def sourceType(self, cls):
        return cls.source.type

# Register your models here.
admin.site.register(Article, ArticleTable)
