from django.db import models

# Create your models here.
class Supervisor(models.Model):
    spvsr_name = models.CharField(max_length=20)
    spvsr_id = models.CharField(max_length=10)

    spvsr_onduty = models.BooleanField(default=True)
    spvsr_port = models.CharField(max_length=20)

    spvsr_dutytime_start = models.CharField(max_length=20)
    spvsr_dutytime_end = models.CharField(max_length=20)

    # spvsr_duty : day of week
    spvsr_duty_mon = models.BooleanField(default=True)
    spvsr_duty_tue = models.BooleanField(default=True)
    spvsr_duty_wed = models.BooleanField(default=True)
    spvsr_duty_thu = models.BooleanField(default=True)
    spvsr_duty_fri = models.BooleanField(default=True)
    spvsr_duty_sat = models.BooleanField(default=True)
    spvsr_duty_sun = models.BooleanField(default=True)

    def __str__(self):
        return self.spvsr_name