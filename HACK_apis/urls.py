from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('doctor_api.urls')),
    url(r'^', include('patient_api.urls')),
    url(r'^', include('old_data.urls')),

]
