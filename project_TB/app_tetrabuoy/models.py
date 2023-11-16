from django.db import models

# Create your models here.
class Tetrabuoy(models.Model):
    buoy_name = models.CharField(max_length=20)

    location = models.CharField(max_length=20)
    battery_remain = models.CharField(max_length=20)
    led_power = models.CharField(max_length=20)

    # sensor_1 = 0
    # sensor_2 = 0
    # sensor_3 = 0

    # battery_settings = 0
    # led_settings = 0
    # realtime_video = 0 

    def __str__(self):
        return self.buoy_name