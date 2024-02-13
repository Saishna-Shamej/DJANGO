from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mee(request):
    return HttpResponse("Hello world")

def home(request):
    return render(request,'home.html')