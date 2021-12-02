from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from .serializers import weatherSerializer


from .weatherMapper import getData, mapToWeatherModel, mapOneCallToWeatherModel

apikey = 'bec349f77465cc15eded6e1c76e97b34'
baseUrl = 'https://api.openweathermap.org/data/2.5/'


# sample request http://127.0.0.1:7001/weatherByCity/?city=Cairo
class weatherByCity(APIView):

    def get(self, request):
        city = request.query_params.get('city')
        print(city)

        params = {
            "q": city,
            "units": "metric",
            "appid": apikey
        }
        url = baseUrl + 'weather?'

        serializer = weatherSerializer(mapToWeatherModel(url, params), many=False)
        return Response(serializer.data)


# sample request http://127.0.0.1:8000/weatherByLongLatAndDate/?lat=60.99&lon=30.9&date=5-11-2021

class weatherByLongLatAndDate(APIView):
    def get(self, request):
        latitude = request.query_params.get('lat')
        longitude = request.query_params.get('lon')
        date = request.query_params.get('date')

        # TODO:if missing params...

        print("TESTOWY TEKST")

        params = {
            "lat": latitude,
            "lon": longitude,
            "units": "metric",
            "appid": apikey,
            "dt": int(datetime.datetime.strptime(date, "%d-%m-%Y").timestamp())
        }
        url = baseUrl + 'onecall/timemachine?'

        serializer = weatherSerializer(mapOneCallToWeatherModel(url, params), many=False)
        return Response(serializer.data)
