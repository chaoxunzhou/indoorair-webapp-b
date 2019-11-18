from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, response, views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from gateway.serializers import LoginSerializer, RegisterSerializer


def register_page(request):
   return render(request, "gateway/register.html", {})


class AccountRegisterAPI(views.APIView):

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            status = status.HTTP_201_CREATED,
            data = serializer.data,
        )

# http --form POST http://127.0.0.1:8000/api/register username=ydang5 password=123 first_name=yi last_name=dang email=y@y.com


def register_ok_page(request):
    return render(request, "gateway/register_ok_page.html",{})


def login_page(request):
   user = request.user
   return render(request, "gateway/login.html", {})


class AccountLoginAPI(views.APIView):
    def post(self, request):

        login_serializer = LoginSerializer(data = request.data,context={
            'request':request,
        })
        login_serializer.is_valid(raise_exception=True)
        login_serializer.save()

        return response.Response(
            status=status.HTTP_201_CREATED,
            data = {
                    'message': 'Login successfully.',
                })

# http --session=user1 --form POST http://127.0.0.1:8000/api/login username="ydang5" password="123"

def logout_page(request):
   user = request.user
   return render(request, "gateway/logout.html", {})


class AccountLogoutAPI(views.APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return response.Response(
            status=status.HTTP_200_OK,
            data = {
                'message': 'You have been logged out',
            })

        else:
            return response.Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data = {
                'message': 'Please login first',
        })
# http --session=user1 --form POST http://127.0.0.1:8000/api/logout
# Error message: TypeError: 'type' object is not iterable
