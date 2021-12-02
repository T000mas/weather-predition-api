from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime

import requests


# example: http://127.0.0.1:7002/simplePrediction/getPredictionByCity/?city=Warszawa
class getPredictionByCity(APIView):
    def get(self, request):
        city = request.query_params.get('city')
        address = 'http://127.0.0.1:7001/weatherByCity/?city=' + city.replace('/','')
        weatherData = requests.get(address).json()
        
        if weatherData['temp'] < 15:
            probability = 0.0
        elif weatherData['temp'] < 25:
            probability = 0.2
        elif weatherData['temp'] < 30:
            probability = 0.5
        else:
            probability = 0.8

        response = JsonResponse({
            'probability':probability
        })
        return response


# example: http://127.0.0.1:7002/simplePrediction/getPredictionByCoordinates/?lat=60.99&lon=30.9
class getPredictionByCoordinates(APIView):
    def get(self, request):
        latitude = request.query_params.get('lat')
        longitude = request.query_params.get('lon')
        date = datetime.today().strftime('%d-%m-%Y')

        address = 'http://127.0.0.1:7001/weatherByLongLatAndDate/?lat=' + latitude + '&lon=' + longitude.replace('/','') + '&date=' + date
        weatherData = requests.get(address).json()

        if weatherData['temp'] < 15:
            probability = 0.0
        elif weatherData['temp'] < 25:
            probability = 0.2
        elif weatherData['temp'] < 30:
            probability = 0.5
        else:
            probability = 0.8

        response = JsonResponse({
            'probability':probability
        })
        return response
