from rest_framework import serializers
from .models import Doctor, Speciality, Appointment

class SpecialitySerializer(serializers.ModelSerializer):
    doctors = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    class Meta:
        model = Speciality
        fields = ['id', 'title', 'doctors']
        # multiplechoices = serializers.MultipleChoiceField(choices = TIME_AVAILABLE_CHOICES)


class DoctorSerializer(serializers.ModelSerializer):
    speciality = serializers.PrimaryKeyRelatedField(queryset=Speciality.objects.all(), many=False)
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'speciality']



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'schedule_date', 'doctor', 'time_selected']