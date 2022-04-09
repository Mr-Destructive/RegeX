from dateutil import parser
from fetcher.models import PodLinks, Episode
import feedparser
import ssl

if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context


def fetch_podcasts():

    feedlist = PodLinks.objects.values_list("link", flat=True)
    for feed in feedlist:
        feed = feedparser.parse(feed)

        for item in feed.entries:
            if not Episode.objects.filter(title=item.title).exists():
                audio_link = item.links[1].href
                print(audio_link)
                if "href" in feed.feed.image:
                    image = feed.feed.image.href
                tags = []
                description = ""
                if "description" in item:
                    description = item.description.lower()

                if "tags" in item:
                    for tag in item["tags"]:
                        if "term" in tag:
                            tags.append(tag["term"].lower())
                        else:
                            tags.append(tag.lower())
                episode = Episode(
                    title=item.title,
                    description=description,
                    audio_link=audio_link,
                    link=item.link,
                    tags=tags,
                    image=image,
                )
                episode.save()
