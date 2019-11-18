"""
dashboard/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('api/dashboard', views.DashboardApi.as_view()),
]
