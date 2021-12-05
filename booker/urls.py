# created this new ULS file

from django.urls import path
from booker import views # added new line

urlpatterns = [
    path('speciality/', views.SpecialityList),
    # path('appointments/', views.AppointmentList),
]