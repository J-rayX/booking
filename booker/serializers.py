from rest_framework import serializers
from .models import Doctor, Speciality, Appointment


# import requests
from django.core.mail import send_mail

class DoctorSerializer(serializers.ModelSerializer):
    speciality = serializers.PrimaryKeyRelatedField(queryset=Speciality.objects.all(), many=False)
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'speciality']


class SpecialitySerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True)
    class Meta:
        model = Speciality
        fields = '__all__'



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'schedule_date', 'doctor', 'time_selected']

    def send_dynamic_mail(self, doctor, schedule_date, time_selected):
        from_email = 'jkaylight@gmail.com'
        doctor_details = Doctor.objects.get(name=doctor)
        to_email = doctor_details.email
        send_mail(
            'New consultation booked',
            'An appointment has been scheduled for {} on {}'.format(schedule_date, time_selected),
            from_email,
            [to_email],
            fail_silently=False,
        )

    def create(self, validated_data):
        appointment = Appointment.objects.create(**validated_data)

        doctor = validated_data.get('doctor')  
        schedule_date = validated_data.get('schedule_date')
        time_selected = validated_data.get('time_selected')

        self.send_dynamic_mail(doctor, schedule_date, time_selected)
        return appointment