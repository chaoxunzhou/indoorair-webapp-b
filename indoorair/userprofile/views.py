"""
homepage/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect


def profile_retrieve_page(request):
    return render(request, "userprofile/retrieve.html", {})


def get_profile_retrieve_api(request):
    return JsonResponse({
         'first_name': request.user.first_name,
         'last_name': request.user.last_name,
         'email': request.user.email,
         'username': request.user.username,
    })


def profile_update_page(request):
    return render(request, "userprofile/update.html", {})


def post_profile_update_api(request):
    return JsonResponse({
         'version': '1.0',
    })
