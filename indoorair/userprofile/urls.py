"""
userprofile/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.profile_retrieve_page, name='profile_retrieve_page'),
    path('api/profile', views.get_profile_retrieve_api, name='profile_retrieve_api'),
    path('profile/update', views.profile_update_page, name='profile_update_page'),
    path('api/profile/update', views.post_profile_update_api, name='profile_update_api'),

]
