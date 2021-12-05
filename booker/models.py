from django.db import models

# Create your models here.

class Speciality(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    TIME_AVAILABLE_CHOICES = [
        ('9am', '9am - 10am'),
        ('10am', '10am - 11am'),
        ('11am', '11am - 12pm'),
        ('12am', '12pm - 1pm'),
        ('1pm', '1pm - 2pm'),
        ('2pm', '2pm - 3pm'),
        ('3pm', '3pm - 4pm'),
    ]
    time_available = models.CharField(max_length=4, choices=TIME_AVAILABLE_CHOICES)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    time_selected = models.CharField(max_length=255)

    # TIME_AVAILABLE_CHOICES = [
    #     ('9am', '9am - 10am'),
    #     ('10am', '10am - 11am'),
    #     ('11am', '11am - 12pm'),
    #     ('12am', '12pm - 1pm'),
    #     ('1pm', '1pm - 2pm'),
    #     ('2pm', '2pm - 3pm'),
    #     ('3pm', '3pm - 4pm'),
    # ]
    # time_selected = models.CharField(max_length=2, choices=TIME_AVAILABLE_CHOICES)
