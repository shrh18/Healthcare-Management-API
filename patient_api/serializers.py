from rest_framework import serializers
from patient_api.models import PatientApi


class PatientApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientApi
        fields = ('patient_name',
                  'gender',
                  'address',
                  'number',
                  'appointment_date', 'time',
                  'doctor_name',
                  'hospital_name',
                  'description')
