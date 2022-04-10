from django.urls import path
from django.views.generic import TemplateView
from .views import home, podcast, live_price, about, contact, subscription

urlpatterns = [
    path("", home, name="home"),
    path("podcast/", podcast, name="podcast"),
    path("prices/", live_price, name="price"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("subscription/", subscription, name="subscription"),
]
