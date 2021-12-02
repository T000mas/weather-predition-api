import urllib
import requests

from webapp.models import weatherData


def getData(url, params):
    return requests.get(url + urllib.parse.urlencode(params)).json()


def mapToWeatherModel(url, params):
    weatherJson = getData(url, params)

    date = weatherJson["dt"]
    temp = weatherJson["main"]["temp"]
    feels_like = weatherJson["main"]["feels_like"]
    wind_speed = weatherJson["wind"]["speed"]
    pressure = weatherJson["main"]["pressure"]
    humidity = weatherJson["main"]["humidity"]
    visibility = weatherJson["visibility"]
    description = weatherJson["weather"][0]["description"]
    main = weatherJson["weather"][0]["main"]
    longitude = weatherJson["coord"]["lon"]
    latitude = weatherJson["coord"]["lat"]

    return weatherData(date, temp, feels_like, wind_speed, pressure, humidity, visibility, description, main, longitude, latitude)


def mapOneCallToWeatherModel(url, params):
    weatherJson1 = getData(url, params)
    weatherJson = weatherJson1["current"]

    date = weatherJson["dt"]
    temp = weatherJson["temp"]
    feels_like = weatherJson["feels_like"]
    wind_speed = weatherJson["wind_speed"]
    pressure = weatherJson["pressure"]
    humidity = weatherJson["humidity"]
    visibility = weatherJson["visibility"]
    description = weatherJson["weather"][0]["description"]
    main = weatherJson["weather"][0]["main"]

    return weatherData(date, temp, feels_like, wind_speed, pressure, humidity, visibility, description, main)