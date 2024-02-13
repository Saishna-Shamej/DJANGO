from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from.models import product
def index(request):
    return HttpResponse("HELLO")

def ind(request):
    items={
        'item' : product.objects.all()
    }
    return render(request,'index.html',items)
