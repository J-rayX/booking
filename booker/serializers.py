from rest_framework import serializers
from .models import Doctor, Speciality, Appointment


class DoctorSerializer(serializers.ModelSerializer):
    speciality = serializers.PrimaryKeyRelatedField(queryset=Speciality.objects.all(), many=False)
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'speciality']


class SpecialitySerializer(serializers.ModelSerializer):
    # doctors = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    doctors = DoctorSerializer(many=True)
    class Meta:
        model = Speciality
        # fields = ['id', 'title', 'doctors']
        fields = '__all__'
        # multiplechoices = serializers.MultipleChoiceField(choices = TIME_AVAILABLE_CHOICES)



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'schedule_date', 'doctor', 'time_selected']