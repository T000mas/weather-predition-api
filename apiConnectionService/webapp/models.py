from django.db import models


class weatherData(models.Model):
    date = models.CharField(max_length=100)
    temp = models.FloatField()
    feels_like = models.FloatField()
    wind_speed = models.FloatField
    pressure = models.FloatField()
    humidity = models.FloatField()
    visibility = models.FloatField()
    description = models.CharField(max_length=1000)
    # Group of weather parameters (Rain, Snow, Extreme etc.)
    main = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __init__(self, date, temp, feels_like, wind_speed, pressure, humidity, visibility, description, main, longitude = 0, latitude = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date = date
        self.temp = temp
        self.feels_like = feels_like
        self.wind_speed = wind_speed
        self.pressure = pressure
        self.humidity = humidity
        self.visibility = visibility
        self.description = description
        self.main = main
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return self.date, self.temp, self.feels_like, self.wind_speed, self.pressure, self.humidity, self.visibility, self.description, self.main, self.longitude, self.latitude
