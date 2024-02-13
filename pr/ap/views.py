from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("hello world")

def people(request):
    return render(request,'my html file.html')
