from django.db import models

# Create your models here.

class Speciality(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    speciality = models.ForeignKey(Speciality, related_name='doctors', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    time_selected = models.CharField(max_length=255)

    class Meta:
        unique_together = ('doctor', 'schedule_date', 'time_selected',)