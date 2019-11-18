"""
homepage/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('api/version', views.get_version_api, name='version_api'),
]
