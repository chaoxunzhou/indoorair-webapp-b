from rest_framework import views,response,status
from django.shortcuts import render
from django.http import JsonResponse

from dashboard.serializers import AverageCalculatorSerializer,AddSerializer
from foundations.models import MakeItUnique, Instrument, Sensor, TimeSeriesDatum



def dashboard_page(request):
    return render(request, "dashboard/dashboard.html", {})


class DashboardAPIView(views.APIView):
    def post(self, request):
        if request.user.is_authenticated:
            serializer = AddSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Response(
            status = status.HTTP_200_OK,
            data = {
            'message': 'Add the sensor.'
            }
            )
        else:
             return response.Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data = {
                'message': 'Please log in.',
            }
        )

    def make_average(self, data):
        sum=0
        for datum in data:
            sum = sum + datum
            average = sum/len(data)

        return average

    def get(self, request):
        try:
            Temperature = TimeSeriesDatum.objects.filter(name='Temperature').values_list('value', flat=True)
            Humidity = TimeSeriesDatum.objects.filter(name='Humidity').values_list('value', flat=True)
            Pressure = TimeSeriesDatum.objects.filter(name='Pressure').values_list('value', flat=True)
            Co2 = TimeSeriesDatum.objects.filter(name='Co2').values_list('value', flat=True)
            TVOC = TimeSeriesDatum.objects.filter(name='TVOC').values_list('value', flat=True)
        except Exception as e:
            return response.Response(
            status = status.HTTP_400_BAD_REQUEST,
            data = {
                'message': str(e)
                }
            )

        avg_temperature = make_average(Temperature, many=False)
        avg_humidity = make_average(Humidity, many=False)
        avg_pressure = make_average(Pressure, many=False)
        avg_Co2 = make_average(Co2, many=False)
        avg_TVOC = make_average(TVOC, many=False)

        return response.Response(
            status=status.HTTP_200_OK,
            data={
                'temperature_sensor': 'Average Temperature = ' + avg_temperature.data,
                'humidity_sensor': 'Average Humidity = ' + avg_temperature.data,
                'pressure_sensor': 'Average Pressure = ' + avg_press.data,
                'CO2_sensor': 'Average CO2 = ' + avg_co2.data,
                'TVOC_Sensor': 'Average TVOC = ' + avg_tvoc.data,
            }
        )
