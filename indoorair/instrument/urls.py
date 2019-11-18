"""
instrument/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('instrument/create', views.i_create_page, name='i_create_page'),
    path('instruments', views.i_list_page, name='i_list_page'),
    path('instrument/<id>', views.i_retrieve_page, name='i_retrieve_page'),
    path('instrument/<id>/update', views.i_update_page, name='i_update_page'),
    path('api/instruments', views.get_instruments_list_api, name='instruments_api'),
    path('api/instruments/create', views.post_instruments_create_api, name='instrument_create_api'),
    path('api/instrument/<id>', views.i_retrieve_api, name='i_retrieve_api'),
    path('api/instrument/<id>/update', views.i_update_api, name='i_update_api'),
]
