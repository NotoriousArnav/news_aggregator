from django.contrib import admin
from .models import *

class ArticleTable(admin.ModelAdmin):
    list_display = ["source", "sourceType", "title", "description", "md5hash", "datetime"]

    def sourceType(self, cls):
        return cls.source.type

# Register your models here.
admin.site.register(Article, ArticleTable)
