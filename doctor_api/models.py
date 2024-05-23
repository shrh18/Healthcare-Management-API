from django.db import models
from datetime import timedelta
from six import python_2_unicode_compatible
from multiselectfield import MultiSelectField


class DoctorApi(models.Model):
    doctor_name = models.CharField(max_length=100, blank=False, default='')
    hospital_name = models.CharField(max_length=100, blank=False, default='')
    patient_name = models.CharField(max_length=100, blank=False, default='')
    patient_age = models.IntegerField()
    patient_weight = models.IntegerField()
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    appointment_date = models.DateField()
    symptoms = models.TextField()
    diagnosis = models.TextField()
    medicine = models.TextField()
    days = models.IntegerField()
    MY_CHOICES = (('B', 'Breakfast'),
                  ('L', 'Lunch'),
                  ('D', 'Dinner'),
                  ('B-L', 'Breakfast-Lunch'),
                  ('L-D', 'Lunch-Dinner'),
                  ('B-D', 'Breakfast-Dinner'),
                  ('B-L-D', 'Breakfast-Lunch-Dinner'),)
    interval = models.CharField(max_length=10, choices=MY_CHOICES)
    recommendation = models.CharField(max_length=100, blank=False, default='')


class Meta:
    ordering = ['appointment_date']
