from django.contrib import admin
from .models import Speciality, Doctor, Appointment # added new line


# Register your models here.

admin.site.register(Speciality)
admin.site.register(Doctor)
admin.site.register(Appointment)