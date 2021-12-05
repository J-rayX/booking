from django.shortcuts import render
from rest_framework import generics # added new line
from .models import Doctor, Speciality, Appointment # added new line
from .serializers import SpecialitySerializer, DoctorSerializer, AppointmentSerializer # added new line

# Create your views here.
class SpecialityList(generics.ListCreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    name = 'speciality-list'

class DoctorList(generics.ListCreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    name = 'speciality-list'