from rest_framework import serializers
from doctor_api.models import DoctorApi


class DoctorApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorApi
        fields = ('doctor_name', 
                  'hospital_name',
                  'patient_name',
                  'patient_age',
                  'patient_weight',
                  'gender',
                  'appointment_date',
                  'symptoms',
                  'diagnosis',
                  'medicine',
                  'days',
                  'interval',
                  'recommendation')
