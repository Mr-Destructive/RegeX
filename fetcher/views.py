from django.shortcuts import render
from .models import Article, Episode, BlogLink, PodLinks
import random
import requests


def home(request):
    context = {}

    articles_list = Article.objects.values()
    podcast_list = Episode.objects.values()
    context["articles"] = articles_list
    context["podcast"] = []
    total_articles = len(articles_list)
    context["featured_article"] = articles_list[random.randint(0, total_articles)]
    context["list_articles"] = random.sample(list(articles_list), 15)

    return render(
        request,
        "index.html",
        {
            "articles": random.sample(list(articles_list), 15),
            "featured_article": context["featured_article"],
            "list_articles": context["list_articles"],
        },
    )


def podcast(request):
    context = {}

    podcast_list = Episode.objects.values()
    context["podcast"] = random.sample(list(podcast_list), 15)
    total_podcast = len(podcast_list)

    return render(
        request,
        "fetcher/podcast.html",
        {
            "podcasts": context["podcast"][:15],
        },
    )


def live_price(request):
    data = {}
    data["crypto_data"] = get_crypto_data()
    print(data)
    return render(request, "fetcher/live.html", data)


def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"

    try:
        print(requests.get(api_url).json())
        data = requests.get(api_url).json()
    except Exception as e:
        data = dict()

    return data


def about(request):
    return render(request, "fetcher/about.html")


def contact(request):
    return render(request, "fetcher/contact.html")


def subscription(request):
    return render(request, "fetcher/subscription.html")
