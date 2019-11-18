# def post_register_api(request):
#     first_name = request.POST.get("first_name")
#     last_name = request.POST.get("last_name")
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     username = request.POST.get("username")
#
#     # This is for debugging purposes only.
#     print(first_name, last_name, username, email, password)
#
#     # STEP 3: Plug in our data from the request into our `User` model.
#     try:
#         user = User.objects.create_user(username, email, password)
#         user.last_name = last_name
#         user.first_name = first_name
#         user.save()
#
#         return JsonResponse({
#              'was_registered': True,
#              'reason': None,
#         })
#     except Exception as e:
#         return JsonResponse({
#              'was_registered': False,
#              'reason': str(e),
#         })
#
#
#
from rest_framework import serializers # (1) NEED TO IMPORT CLASS
from foundation.models import ArchivedWebPage # (2) OPTIONAL - IMPORT ANY MODELS WE USE
from rest_framework.validators import UniqueTogetherValidator


class RegisterApiSrializers(serializers.Serializer):
    first_name = serializers.CharField(required = False)
    last_name = serializers.CharField(required = False)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())
    )
    password = serializers.CharField()

    def create(self, validated_data):
        first_name = validated_data.get('first_name',None)
        last_name = validated_data.get('last_name',None)
        email = validated_data.get('email')
        username = validated_data.get('username')
        password = validated_data.get('password')
        newuser = user.object.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = password,
        )
        newuser.save()
        return newuser
