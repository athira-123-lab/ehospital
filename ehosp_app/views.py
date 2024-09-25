
import stripe
from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from urllib3 import request

from ehosp_app.models import Patient, Appointment, Doctor, Payment

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

def Delete_patient(request,pid):

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

def Delete_doctor(request,pid):

    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('doctor_details')


def Checkout_session(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        name = request.POST.get('name')
        amount = 100

        line_items = [
            {
                'price_data': {
                    'currency': 'INR',
                    'product_data': {
                        'name': name,
                    },
                    'unit_amount': amount * 100,
                },
                'quantity': 1,
            }
        ]


        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel'))
        )


        return redirect(checkout_session.url, code=303)

    return render(request, 'payment.html')


def success(request):
    amount= Appointment.objects.all()

    return render(request,'success.html')


def cancel(request):
    amount = Appointment.objects.all()

    return render(request, 'cancel.html')


