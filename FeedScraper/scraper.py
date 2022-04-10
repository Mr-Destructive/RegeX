from datetime import datetime
from FeedScraper import fetch_articles, fetch_podcasts
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_articles.fetch_articles, "interval", minutes=60)
    scheduler.add_job(fetch_podcasts.fetch_podcasts, "interval", minutes=60)
    scheduler.start()
