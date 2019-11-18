from rest_framework import status, response, views
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index_page(request):
    user = request.user
    return render(request,'homepage/index.html',{})

def contact_page(request):
        context = {}
        return render(request,'homepage/contact.html',context)

class GetVersion(views.APIView):
    def get(self, request):
        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'version': '0.1.0',
            }
        )
