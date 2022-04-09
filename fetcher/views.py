from django.shortcuts import render
from .models import Article, Episode, BlogLink, PodLinks
import random


def home(request):
    context = {}

    articles_list = Article.objects.values()
    podcast_list = Episode.objects.values()
    context["articles"] = articles_list
    context["podcast"] = []
    total_articles = len(articles_list)
    context["featured_article"] = articles_list[random.randint(0, total_articles)]
    print(context["featured_article"])

    return render(
        request,
        "index.html",
        {
            "articles": context["articles"][:15],
            "featured_article": context["featured_article"],
        },
    )
