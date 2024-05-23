from django.conf.urls import url
from doctor_api import views
from django.urls import path

urlpatterns = [
    url(r'^prescriptions/$', views.prescription_list),
    path('prescriptions/<str:patient_name>/', views.get_event),
    path('prescriptions/doctor/<str:doctor_name>/', views.get_doctor),
    # url(r'^events/upcoming_events$', views.event_list_future),
    # path('events/<str:title>-<str:description>/', views.get_event),
    # url(r'^events/ongoing_events$', views.event_list_ongoing)
]
