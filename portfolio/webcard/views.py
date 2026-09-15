from django.http import HttpResponse
from django.shortcuts import render


def render_webcard(request):
    return render(
        request,
        "webcard/webcard.html"
    )
