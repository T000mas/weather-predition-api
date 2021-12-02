from rest_framework import serializers

from webapp.models import weatherData

class weatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = weatherData
        fields = ('date', 'temp', 'feels_like', 'wind_speed', 'pressure', 'humidity', 'visibility', 'description', 'main', "longitude", "latitude")