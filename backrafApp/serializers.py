from rest_framework import serializers
from .models import StationData, SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class StationDataSerializer(serializers.ModelSerializer):
    sensors = SensorDataSerializer()

    class Meta:
        model = StationData
        fields = '__all__'
