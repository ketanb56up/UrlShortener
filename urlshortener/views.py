from django.http import HttpResponse
from django.shortcuts import redirect

from .models import UrlData

import string
import random


def urlShort(request):
    if request.method == 'GET':
        original_url = request.GET.get("original_url")
        if original_url is not None:
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            new_url = UrlData(url=original_url, slug=slug)
            new_url.save()
            return HttpResponse("short url is " + slug)
    return HttpResponse("Enter the Url in the browser tab.")


def urlRedirect(request, slugs):
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)
