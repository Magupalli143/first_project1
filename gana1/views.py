from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def abc(resquest):
    return HttpResponse('<marquee><h1>GANESH IS GOOD BOY</h1></marquee>')