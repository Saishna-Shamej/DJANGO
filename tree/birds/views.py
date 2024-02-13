from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def nest(request):
    return HttpResponse("Save nature!")

def nature(request):
    return render(request,"nature.html")