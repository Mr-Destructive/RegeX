from django.db import models
from django.contrib.postgres.fields import ArrayField


class BlogLink(models.Model):
    podcast_link = models.URLField(unique=True)
    rss_link = models.URLField(unique=True)


class Article(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    link = models.URLField(unique=True)
    tags = ArrayField(models.CharField(max_length=128))
    image = models.URLField(unique=True)
    publication_name = models.CharField(max_length=2048)

    def __str__(self) -> str:
        return f"{self.title}"


class PodLinks(models.Model):
    publication_name = models.CharField(max_length=256, unique=True)
    publication_logo = models.CharField(max_length=2048)
    description = models.CharField(max_length=2048)
    link = models.URLField(max_length=2048, unique=True)

    def __str__(self) -> str:
        return f"{self.publication_name}"


class Episode(models.Model):
    title = models.CharField(max_length=2048, unique=True)
    description = models.TextField()
    link = models.URLField(max_length=2048)
    tags = ArrayField(models.CharField(max_length=256))
    image = models.URLField(max_length=2048)
    audio_link = models.URLField(max_length=2048)
    publication_name = models.ForeignKey(PodLinks, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"
