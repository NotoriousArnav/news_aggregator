from django.db.models.signals import post_save
from django.dispatch import receiver
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_feed
from RSS_Sources.models import Source, RSS_Cache
import feedparser

scheduler = BackgroundScheduler()

# @receiver(post_save, sender=RSS_Cache)
# def process(sender, instance, **kwargs):
#     data = feedparser.parse(instance.cache)
#     for x in data.entries[5:]:
#         print(x.title)
#         print(x.description)
#         print(x['content'])

@receiver(post_save, sender=Source)
def update_scheduler(sender, instance, **kwargs):
    global scheduler
    if scheduler.running:
        scheduler.shutdown()
        scheduler = BackgroundScheduler()
        sources = Source.objects.all()
        for source in sources:
            print(f"Added RSS Job for Source: {source} with interval {source.update_interval} minutes")
            scheduler.add_job(get_feed, 'interval', seconds=source.update_interval*60, args=[source])
        scheduler.start()

def start():
    sources = Source.objects.all()
    for source in sources:
        print(f"Added RSS Job for Source: {source} with interval {source.update_interval} minutes")
        scheduler.add_job(get_feed, 'interval', seconds=source.update_interval*60, args=[source])
    scheduler.start()
