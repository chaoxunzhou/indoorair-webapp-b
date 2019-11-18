from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from foundation.models import Instrument, Sensor, TimeSeriesDatum


class SensorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[
        UniqueValidator(queryset=ArchivedWebpage.objects.all()))
