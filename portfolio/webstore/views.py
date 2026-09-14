from django.http import HttpResponse
from django.shortcuts import render


def render_webstore(request):
    return render(
        request,
        "webstore/webstore.html"
    )
