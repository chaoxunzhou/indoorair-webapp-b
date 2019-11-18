from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('api/dashboard',views.DashboardAPIView.as_view()),
    path('api/list-instrument',views.ListInstrumentAPIView.as_view()),
]
