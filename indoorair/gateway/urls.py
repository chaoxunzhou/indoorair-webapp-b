"""
homepage/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_page, name='register_page'),
    path('register/success', views.register_success_page, name='register_success_page'),
    path('login', views.login_page, name='login_page'),
    path('api/regsiter', views.RegisterApi.as_view()),
    path('api/login', views.post_login_api, name='login_api'),
    path('logout', views.logout_page, name='logout_page'),
    path('api/logout', views.post_logout_api, name='logout_api'),

]
