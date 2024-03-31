from django.conf import settings
from RSS_Sources.models import *
import requests

def get_feed(source):
    print(f"""Updating "{source.name}" from RSS Url {source.rss_feed_link}.
Next Update in {source.update_interval} minutes""")
    string = requests.get(source.rss_feed_link).text.strip()
    obj = RSS_Cache.objects.filter(source=source).first()
    try:
        latest_cache = obj.cache
    except:
        latest_cache = None
    if (latest_cache == None) or (string != latest_cache):
        print("Updating")
        RSS_Cache.objects.create(
            source=source,
            cache=string
        )
        print("Updated")