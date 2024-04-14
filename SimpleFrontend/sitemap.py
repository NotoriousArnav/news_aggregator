from django.contrib.sitemaps import Sitemap
from articles.models import Article

class ArticleSiteMap(Sitemap):
    priority = 1

    def items(self):
        return [x for x in Article.objects.all().order_by('-datetime')]

    def lastmod(self, obj):
        return obj.datetime
