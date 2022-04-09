from datetime import datetime
from FeedScraper import fetch_articles
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_articles.fetch_articles, "interval", minutes=1)
    scheduler.start()
