from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import statistics

from foundations.models import MakeItUnique


id = MakeItUnique.IntegerField(read_only=True)
value = MakeItUnique.IntegerField(
     validators = [
     UniqueValidator(queryset=MakeItUnique.objects.all())
     ]
)


class AddSerializer(serializers.Serializer):
    def create(self, validated_data):
        value = validated_data.get('value')
        name = validated_data.get('name')
        memory = MakeItUnique.objects.create(name= name,value=value)
        memory.save()
        return memory



class CalculatorSerializer(serializers.Serializer):
    def post(self, data):
        sum=0
        for datum in data:
            sum = sum + datum
            average = sum/len(data)
        return average
