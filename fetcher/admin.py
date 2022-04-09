from django.contrib import admin
from .models import BlogLink, PodLinks
from fetcher.models import PodLinks

admin.site.register(BlogLink)
admin.site.register(PodLinks)
