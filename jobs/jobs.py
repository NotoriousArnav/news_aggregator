import requests, feedparser, hashlib, calendar
from django.conf import settings
from RSS_Sources.models import *
from articles.models import *
from datetime import datetime

def date_to_datetime(date_string, date_format="%a, %d %b %Y %H:%M:%S %z"):
    # Parse the date string into a datetime object
    try:
        date_obj = datetime.strptime(date_string, date_format)
    except:
        try:
            date_obj = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S %Z")
        except:
            date_obj = datetime.fromisoformat(date_string)
    return date_obj

def parse_feed(feed_):
    feed = feedparser.parse(feed_)
    entries = []
    for entry in feed.entries:
        title = entry.title
        if 'content' in entry:
            content = entry.content[0].value
        elif 'content_encoded' in entry:
            content = entry.content_encoded
        elif 'dc_content' in entry:
            content = entry.dc_content
        elif 'summary' in entry:
            content = entry.summary
        else:
            content = "Content: Not Available"
        try:
            thumbnail = entry.media_thumbnail[0]['url']
        except:
            thumbnail = [x for x in entry.links if x['rel'] == 'enclosure'][0]['href']
        entries.append((title, content, entry.summary, date_to_datetime(entry.published), entry.link, thumbnail))
    return entries

def make_articles():
    qry_set = RSS_Cache.objects.filter(processed=False)
    for x in qry_set:
        y = parse_feed(x.cache)
        for f in y:
        #    print(f[0], f[1][:20], f[2], f[3], sep="...")
            content = f"""{f[0]}{f[2]}{f[1]}""".encode()
            digest = hashlib.md5(content).hexdigest()
            try:
                article, created = Article.objects.get_or_create(
                    title = f[0],
                    content = f[1],
                    description = f[2],
                    datetime = f[3],
                    link = f[4],
                    thumbnail = f[5],
                    source = x.source,
                    md5hash_value = digest,
                )
            except Exception as e:
                if isinstance(e, Article,MultipleObjectsReturned):
                    pass
                elif isinstance(e, Article.DoesNotExist):
                    print(e)
        x.processed = True
        x.save()

def delete_dupes():
    from collections import Counter

# Get all articles from the database
    articles = Article.objects.all()

# Create a Counter object to count the occurrences of each md5hash
    hash_counter = Counter(article.md5hash_value for article in articles if article.md5hash_value)

# Get the md5hash values that occur more than once (duplicates)
    duplicate_hashes = [hash for hash, count in hash_counter.items() if count > 1]

# Iterate over the duplicates and delete them
    for hash in duplicate_hashes:
        duplicate_articles = Article.objects.filter(md5hash_value=hash)[1:]
        for article in duplicate_articles:
            article.delete()

def delete_cache():
    qry_set = RSS_Cache.objects.filter(processed=True)
    for x in qry_set:
        x.delete()
    
def get_feed(source):
    string = requests.get(source.rss_feed_link).text.strip()
    obj = RSS_Cache.objects.filter(source=source).first()
    try:
        latest_cache = obj.cache
    except:
        latest_cache = None
    if (latest_cache == None) or (string != latest_cache):
        RSS_Cache.objects.create(
            source=source,
            cache=string
        )

def update_keywords():
    import time
    qry_set = Article.objects.filter(keywords='')
    for x in qry_set:
        time.sleep(2)
        x.save()