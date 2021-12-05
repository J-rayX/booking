# created this new ULS file

from django.urls import path
from booker import views # added new line

urlpatterns = [
    path('speciality/', views.SpecialityList.as_view(), name = 'speciality-list'),
    path('doctors/', views.DoctorList.as_view(), name = 'doctors-list'),
    # path('appointments/', views.AppointmentList),
]