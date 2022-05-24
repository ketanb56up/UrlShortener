from django.urls import path
from .views import urlShort, urlRedirect

urlpatterns = [
    path("", urlShort, name="home"),
    path("<str:slugs>", urlRedirect, name="redirect")  # create, replied and bounced msg
]
