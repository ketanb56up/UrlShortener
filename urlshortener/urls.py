from django.urls import path
from .views import index

urlpatterns = [
    path('event', index),  # create, replied and bounced msg
]
