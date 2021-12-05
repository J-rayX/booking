# created this new ULS file

from django.urls import path
from booker import views

urlpatterns = [
    path('speciality/', views.SpecialityList),
    path('appointments/', views.AppointmentsList),
]