from django.urls import path,include


from . import views

from .views import *

urlpatterns=[
    path('register/',views.Register,name='register'),
    path('',views.Login,name='login'),
    path('home/',views.Home,name='home'),
    path('logout/',views.Logout,name='logout'),
    path('patient_details/',views.Patient_details,name='patient_details'),
    path('add_patient/', views.Add_patient, name='add_patient'),
    path('delete_patient/', views.Delete_patient, name='delete_patient'),
    path('schedule/', views.Schedule, name='schedule'),
    path('booking/', views.Booking, name='booking'),
    path('delete_appointment/', views.Delete_appointment, name='delete_appointment'),
    path('view_prescription/', views.View_prescription, name='view_prescription'),
    path('delete_prescription/', views.Delete_prescription, name='delete_prescription'),
    path('add_prescription/', views.Add_prescription, name='add_prescription'),
    path('add_doctor/', views.Add_doctor, name='add_doctor'),
    path('doctor_details/', views.Doctor_details, name='doctor_details'),
    path('delete_doctor/', views.Delete_doctor, name='delete_doctor'),

]

