# from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import feed_update

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(feed_update, 'interval', seconds=5*60)
	scheduler.start()