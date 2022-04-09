from django.apps import AppConfig


class FetcherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fetcher"

    def ready(self):
        from FeedScraper import scraper

        scraper.start()
