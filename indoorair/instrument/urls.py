from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('instrument/create', views.i_create_page, name='i_create_page'),
    path('instrument/list', views.i_list_page, name='i_list_page'),
    path('instrument/retrieve', views.i_retrieve_page, name='i_retrieve_page'),
    path('instrument/update', views.i_update_page, name='i_update_page'),
    path('api/instruments/create', views.InstrumentCeateAPI.as_view()),
    path('api/instruments', views.InstrumentListAPIView.as_view()),
    path('api/instrument/<id>', views.InstrumentRetrieveUpdateAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
