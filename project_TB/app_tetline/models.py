from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Tetline(models.Model):
    line_name = models.CharField(max_length=20)

    location = models.CharField(max_length=20)
    led_power = models.CharField(max_length=20)
    sound_power = models.CharField(max_length=20)

    # line_settings = 0
    # led_settings = 0
    # sound_settings = 0 

    def __str__(self):
        return self.line_name