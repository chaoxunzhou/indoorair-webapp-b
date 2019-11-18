from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render # STEP 1 - Import
from django.shortcuts import redirect
from rest_framework import status, views, response
from django.shortcuts import get_object_or_404

from foundation.models import Instrument
from instrument.serializers import InstrumentSerializer


def i_list_page(request):
    return render(request, "instrument/list.html", {})

def i_create_page(request):
    return render(request, "instrument/create.html", {})


class InstrumentListAPIView(views.APIView):
    def get(self,request):
        instruments = Instrument.objects.filter(user=request.user).values('name','location','serial_number')

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'instrument list: ': instruments,
            }
    )

class InstrumentCeateAPI(views.APIView):
    def post(self ,request):
        serializer = InstrumentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            status = status.HTTP_201_CREATED,
            data = serializer.data,
        )


def i_retrieve_page(request, id):
    return render(request, "instrument/retrieve.html", {
        "instrument_id": int(id),
    })


def i_update_page(request, id):
    return render(request, "instrument/update.html", {
        "instrument_id": int(id),
    })


class InstrumentRetrieveUpdateAPI(views.APIView):
    def get_object(self,id):
        return get_object_or_404(Instrument, id=id)


    def get(self, request, id):
        object = self.get_object(id)
        serializer = InstrumentSerializer(object, many=False)
        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )


    def put(self, request, id):
        object = self.get_object(id)
        serializer = InstrumentSerializer(object, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )
