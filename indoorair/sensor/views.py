from django.shortcuts import render
from rest_framework import status, views, response
from django.shortcuts import get_object_or_404

from foundation.models import Instrument, Sensor, TimeSeriesDatum
from sensor.serializers import SensorSerializer



def sensor_retrieve_page(request, id):
    return render(request, "sensor/retrieve.html", {
        "instrument_id": int(id),
    })


class InstrumentRetrieveUpdateAPI(views.APIView):
    def get_object(self,id):
        return get_object_or_404(Sensor, id=id)


    def get(self, request, id):
        object = self.get_object(id)
        serializer = SensorSerializer(object, many=False)
        return response.Response(
            status = status.HTTP_200_OK,
            data = serializer.data,
        )
