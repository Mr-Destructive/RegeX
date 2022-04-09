from django.urls import path
from django.views.generic import TemplateView
from .views import home, podcast

urlpatterns = [
    path("", home, name="home"),
    path("podcast/", podcast, name="podcast"),
]
