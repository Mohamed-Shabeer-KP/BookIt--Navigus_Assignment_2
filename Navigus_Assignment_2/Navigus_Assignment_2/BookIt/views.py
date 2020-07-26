from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.contrib import messages
from . import custom_auth

def index(request):
    return render(request,'BookIt/index.html')

def login(request):
    if request.method == "POST" :
        if request.POST.get("password") and request.POST.get("email"):
            val_email = request.POST.get("email")            
            val_password = request.POST.get("password")
            user = custom_auth.authenticate(mail=val_email, password=val_password)
            if user is not None:
                messages.info(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Login credetials are invalid')
                return redirect('login')
    else :
        return render(request,'BookIt/login.html')

def register(request):
    if request.method == "POST" :
        if request.POST.get("name") and request.POST.get("password") and request.POST.get("email"):
            val_name = request.POST.get("name")
            val_password = request.POST.get("password")
            val_email = request.POST.get("email")
            try:
                user = User.objects.create_user(val_name,val_email,val_password)
                user.save()
                messages.add_message(request, messages.INFO, 'Hurray! Successfully Registered. Login now !')
                return render(request,'BookIt/login.html')
            except Exception as ex:
                if 'username' in str(ex):
                    messages.add_message(request, messages.INFO, 'OOPS! User name you have entered already exist !')
                else:
                    messages.add_message(request, messages.INFO, 'OOPS! User with an email you have entered already exist !')
                return render(request,'BookIt/registration.html')
    else:
        return render(request,'BookIt/registration.html')

def createSlot(request):
    return redirect('api-slot-web:slot-create')

def viewSlot(request):
    return redirect('api-slot-web:slot-select')

def bookSlot(request):
    return redirect('api-slot-web:slot-update')

def removeSlot(request):
    return redirect('api-slot-web:slot-remove')