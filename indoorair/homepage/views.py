"""
homepage/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect


def index_page(request):
    return render(request, "homepage/index.html", {})


def contact_page(request):
    return render(request, "homepage/contact.html", {})


def get_version_api(request):
    return JsonResponse({
         'version': '1.0',
    })
