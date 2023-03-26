from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, World!')


def welcome(request):
    return render(request, 'app1/welcome.html')


def another(request):
    return render(request, 'app1/dynamic.html', {'Name': "YOGESH"})
