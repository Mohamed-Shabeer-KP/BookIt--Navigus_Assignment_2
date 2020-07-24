from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request,'BookIt/index.html')

def login(request):
    return render(request,'BookIt/login.html')

def register(request):
    return render(request,'BookIt/registration.html')

def features(request):
    return render(request,'BookIt/features.html')