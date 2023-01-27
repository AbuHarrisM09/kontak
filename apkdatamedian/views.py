from django.http import HttpResponse
from django.shortcuts import render

def signin(request):
    return render(request,'sign-in.html')

def dashboard(request):
    return render(request, 'index.html')