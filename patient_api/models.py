from django.db import models
from datetime import timedelta

class PatientApi(models.Model):
    patient_name = models.CharField(max_length = 100, blank = False, default = '')
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address  = models.TextField()
    number = models.IntegerField()
    appointment_date = models.DateField()
    time_CHOICES = (('9:00 - 10:00', '9:00 - 10:00'),
                    ('10:00 - 11:00', '10:00 - 11:00'),
                    ('11:00 - 12:00', '11:00 - 12:00'),
                    ('12:00 - 13:00', '12:00 - 13:00'),)
    time = models.CharField(max_length=15, choices=time_CHOICES)
    # appointment_time_start = models.TimeField()
    # appointment_time_end = models.TimeField()
    doctor_name = models.CharField(max_length=100, blank=False, default='')
    hospital_name = models.CharField(max_length=100, blank=False, default='')
    description = models.TextField()


class Meta:
    ordering = ['appointment_date']
