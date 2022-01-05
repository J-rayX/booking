from django.shortcuts import render

from rest_framework import generics, serializers # added new line
from .models import Doctor, Speciality, Appointment # added new line
from .serializers import SpecialitySerializer, DoctorSerializer, AppointmentSerializer # added new line

# import requests
import json
from django.core.mail import send_mail


# Create your views here.
class SpecialityList(generics.ListCreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    name = 'speciality-list'

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    name = 'doctor-list'

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    # queryset = Appointment.objects.values( 'schedule_date', 'doctor', 'time_selected').distinct()
    # queryset = Appointment.objects.all().distinct()
    serializer_class = AppointmentSerializer
    name = 'appointment-list'
    