from rest_framework import serializers # (1) NEED TO IMPORT CLASS
from foundation.models import IndoorairData # (2) OPTIONAL - IMPORT ANY MODELS WE USE
from rest_framework.validators import UniqueTogetherValidator

MEMORY_ID = 1

class AddSeriliazer(serializers.Serializer):
    value = serializers.FloatField()
    def create(self, validated_data):
        try:
            memory = IndoorairData.object.get(id=MEMORY_ID)
        except IndoorairData.DoesnotExist:
            memory = IndoorairData.object.create(
                id = MEMORY_ID,
                temperature = 0,
                pressure = 0,
                co2 = 0,
                avg_tvoc = 0,
                avg_humidity  = 0,
            )
        temperature = validated_data.get('temperature')
        pressure = validated_data.get('pressure')
        co2 = validated_data.get('co2')
        avg_tvoc = validated_data.get('avg_tvoc')
        avg_humidity = validated_data.get('avg_humidity')
        memory.temperature = (memory.temperature + temperature)/2
        memory.pressure = (memory.temperature + pressure)/2
        memory.co2 = (memory.temperature + co2)/2
        memory.avg_tvoc = (memory.temperature + avg_tvoc)/2
        memory.avg_humidity = (memory.temperature + avg_humidity)/2
        memory.save()

        return memory
