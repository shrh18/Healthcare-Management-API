from django.conf.urls import url
from patient_api import views
from django.urls import path

urlpatterns = [
    url(r'^appointments/$', views.event_list),
    # url(r'^events/(?P<pk>[0-9]+)$', views.event_details),
    # url(r'^events/past_events$', views.event_list_past),
    # url(r'^events/upcoming_events$', views.event_list_future),
    path('appointments/<str:patient_name>/', views.get_event),
    # url(r'^events/ongoing_events$', views.event_list_ongoing)
]
