from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
# from dashboard import views

urlpatterns = [
    path('register', views.register_page, name='register_page'),
    path('api/register', views.AccountRegisterAPI.as_view()),
    path('register/ok', views.register_ok_page, name ='register_ok_page'),
    path('login', views.login_page, name='login_page'),
    path('api/login',views.AccountLoginAPI.as_view()),
    path('logout', views.login_page, name='logout_page'),
    path('api/logout',views.AccountLogoutAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
