from django.contrib import admin

# Register your models here.
from django.contrib import admin
from doctor_api.models import DoctorApi

admin.site.register(DoctorApi)
