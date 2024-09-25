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
    path('delete_patient/?p<int:pid>/', views.Delete_patient, name='delete_patient'),
    path('schedule/', views.Schedule, name='schedule'),
    path('booking/', views.Booking, name='booking'),
    path('delete_appointment/?p<int:pid>/', views.Delete_appointment, name='delete_appointment'),
    path('add_doctor/', views.Add_doctor, name='add_doctor'),
    path('doctor_details/', views.Doctor_details, name='doctor_details'),
    path('delete_doctor/?p<int:pid>/', views.Delete_doctor, name='delete_doctor'),
    path('success/',views.success,name='success'),
    path('cancel/',views.cancel,name='cancel'),
    path('payment/',views.Checkout_session,name='payment')


]

