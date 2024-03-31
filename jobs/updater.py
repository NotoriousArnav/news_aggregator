from django.db.models.signals import post_save
from django.dispatch import receiver
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_feed
from RSS_Sources.models import Source

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
        scheduler.start()

def start():
    sources = Source.objects.all()
    for source in sources:
        print(f"Added RSS Job for Source: {source} with interval {source.update_interval} minutes")
        scheduler.add_job(get_feed, 'interval', seconds=source.update_interval*60, args=[source])
    scheduler.start()