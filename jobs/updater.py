from django.db.models.signals import post_save
from django.dispatch import receiver
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *
from RSS_Sources.models import Source, RSS_Cache

scheduler = BackgroundScheduler()

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
        scheduler.add_job(make_articles, 'interval', seconds=60)
        print("Make Articles Job Added")
        scheduler.add_job(delete_cache, 'interval', seconds=120)
        print("Delete Cache after 90 Seconds Job Addded")
        scheduler.start()

def start():
    sources = Source.objects.all()
    for source in sources:
        print(f"Added RSS Job for Source: {source} with interval {source.update_interval} minutes")
        scheduler.add_job(get_feed, 'interval', seconds=source.update_interval*60, args=[source])
    scheduler.add_job(make_articles, 'interval', seconds=60)
    print("Make Articles Job Added")
    scheduler.add_job(delete_cache, 'interval', seconds=120)
    print("Delete Cache after 90 Seconds Job Addded")
    scheduler.start()
