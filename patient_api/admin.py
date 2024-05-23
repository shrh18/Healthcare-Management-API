from django.contrib import admin

# Register your models here.
from django.contrib import admin
from patient_api.models import PatientApi

admin.site.register(PatientApi)
