from django.conf import settings
from RSS_Sources.models import *
import requests

def feed_update():
    sources = Source.objects.all()
    for source in sources:
        string = requests.get(source.rss_feed_link).text.strip()
        try:
            latest_cache = RSS_Cache.objects.filter(source=source).first().cache
        except:
            latest_cache = None
        if (latest_cache == None) or (string != latest_cache):
            RSS_Cache.objects.create(
                source=source,
                cache=string
            )
        print(f"Cached source: {source}")
    print("Updated Feed Cache")