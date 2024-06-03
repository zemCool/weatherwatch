from django.db import models
from django.contrib.auth.models import User


class Sensor(models.Model):
    SENSOR_TYPES = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=SENSOR_TYPES)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model} - {self.type}"


class Data(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    humidity = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Data from {self.sensor} at {self.timestamp}"


class Alert(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.sensor} at {self.timestamp}"
