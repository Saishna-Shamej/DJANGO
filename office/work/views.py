from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import workerCreationForm


# Create your views here.


def home(request):
    return render(request, 'home.html')

def adminhome(request):
    return render(request, 'adminhome.html')

def staffhome(request):
    return render(request, 'staffhome.html')

def employerhome(request):
    return render(request, 'employerhome.html')

def staffsignup(request):
    form = workerCreationForm(request.POST)
    if request.method == "POST":
        form = workerCreationForm(request.POST)
        if (form.is_valid()):
            f = form.save(commit=False)
            f.is_staff = True
            f.save()
            return home(request)
    return render(request, 'staffsignup.html', {'form': form})

def employersignup(request):
    form = workerCreationForm()
    if request.method == "POST":
        form = workerCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.is_employer = True
            f.save()
            return home(request)
    return render(request, 'employersignup.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user and user.is_superuser == True:
            login(request, user)
            return adminhome(request)
        elif user and user.is_staff == True:
            login(request, user)
            return staffhome(request)
        elif user and user.is_employer == True:
            login(request, user)
            return employerhome(request)
        else:
            return HttpResponse("Invalid login details.....")

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return home(request)