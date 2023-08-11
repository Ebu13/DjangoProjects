from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Home Page')

def courses(request):
    return HttpResponse("Courses List")
