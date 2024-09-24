from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model

from ehosp_app.models import Patient, Appointment, Prescription, Doctor

User = get_user_model()
def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('register')
            else:

                user = User.objects.create_user(username=username,password=password)
                user.name=name
                user.mobile=mobile
                user.save()

                messages.success(request, "User created successfully")
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

def Login(request):


        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                messages.info(request,'please provide correct details')
                return redirect('login')

        return render(request, 'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('login')

def Home(request):
    return render(request,'home.html')

def Patient_details(request):

    patient=Patient.objects.all()
    p={'patient':patient}
    return render(request,'patient_details.html',p)


def Add_patient(request):
    error = None
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        address = request.POST.get('address')
        disease = request.POST.get('disease')

        try:

            Patient.objects.create(
                name=name,
                gender=gender,
                mobile=mobile,
                age=age,
                address=address,
                disease=disease,

            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")


    p = {'error': error}

    return render(request, 'add_patient.html', p)

def Delete_patient(pid):

    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('patient_details')

def Schedule(request):

    appointment=Appointment.objects.all()
    p={'appointment':appointment}
    return render(request,'schedule.html',p)

def Booking(request):

    error = None

    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')


        try:

            Appointment.objects.create(
                name=name,
                date=date,
                time=time,

            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")


    p = {'error': error}

    return render(request, 'booking.html', p)

def Delete_appointment(request,pid):

    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('schedule')

def View_prescription(request):

    prescription=Prescription.objects.all()
    p={'prescription':prescription}
    return render(request,'view_prescription.html',p)

def Delete_prescription(pid):

    prescription=Prescription.objects.get(id=pid)
    prescription.delete()
    return redirect('view_prescription')

def Add_prescription(request):

    error = None

    if request.method == 'POST':

        medicine = request.POST.get('medicine')
        dosage = request.POST.get('dosage')

        try:

            Prescription.objects.create(
                medicine=medicine,
                dosage=dosage,
            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")

    context = {'error': error}
    return render(request, 'add_prescription.html', context)

def Add_doctor(request):
    error = None
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        special= request.POST.get('special')

        try:

            Doctor.objects.create(
                name=name,
                mobile=mobile,
                special=special,


            )
            error = "no"
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")


    p = {'error': error}

    return render(request, 'add_doctor.html', p)

def Doctor_details(request):

    doctor=Doctor.objects.all()
    p={'doctor':doctor}
    return render(request,'doctor_details.html',p)

def Delete_doctor(pid):

    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('doctor_details')
