"""
gateway/views.py
"""
from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from django.contrib.auth.models import User # STEP 1: Import the user
from django.contrib.auth import authenticate, login, logout
from gateway.serializers import RegisterApiSrializers

def register_page(request):
    return render(request, "gateway/register.html", {})


def register_success_page(request):
    return render(request, "gateway/register_success.html", {})


def login_page(request):
    return render(request, "gateway/login.html", {})

class RegisterApi(views.APIViews):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return response.Response(
            status=status.HTTP_201_CREATED,
            data={
            'message':"Your account is created, plz login"
        }
        )


def post_login_api(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    print("For debugging purposes", username, password)

    try:
        user = authenticate(username=username, password=password)
        if user:
            print("PRE-LOGIN", user.get_full_name())
            login(request, user)
            print("POST-LOGIN", user.get_full_name())

            # A backend authenticated the credentials
            return JsonResponse({
                 "was_logged_in": True,
                 "reason": None,
            })
        else:
            # No backend authenticated the credentials
            return JsonResponse({
                 "was_logged_in": False,
                 "reason": "Cannot log in, username or password is wrong.",
            })

    except Exception as e:
        print(e)
        return JsonResponse({
             "was_successful": False,
             "reason": "Cannot log in, username or password is wrong.",
        })



def logout_page(request):
    # STEP 2 - Do something w/ models.
    # ...

    # STEP 3 - Do something w/ context.
    # ..

    # STEP 4 - Use the `render` function.
    return render(request, "gateway/logout.html", {})


def post_logout_api(request):
    try:
        logout(request)
        return JsonResponse({
             "was_logged_out": True,
             "reason": None,
        })
    except Exception as e:
        print(e)
        return JsonResponse({
             "was_logged_out": False,
             "reason": str(e),
        })
