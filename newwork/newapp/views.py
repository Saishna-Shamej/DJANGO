from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .forms import myuserForm, fileForm
from .models import File


# Create your views here.

def home(request):
    return render(request, 'home.html')

def home1(request):
    return HttpResponse("SUCCESSFUL")

def adminhome(request):
    return render(request, 'adminhome.html')

def guesthome(request):
    return render(request, 'guesthome.html')

def ownerhome(request):

    return render(request,'ownerhome.html')

def guestsignup(request):
    form = myuserForm(request.POST)
    if request.method == "POST":
        form = myuserForm(request.POST)
        if (form.is_valid()):
            f = form.save(commit=False)
            f.is_guest = True
            f.save()
            return home(request)
    return render(request, 'guestsignup.html', {'form':form})

def ownersignup(request):
    form = myuserForm()
    if request.method == "POST":
        form = myuserForm(request.POST)
        if form.is_valid():
            f = form.save()
            return home(request)
    return render(request,'ownersignup.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user and user.is_superuser == True:
            login(request, user)
            return adminhome(request)
        elif user and user.is_guest == True:
            login(request, user)
            return guesthome(request)
        elif user and user.is_owner == True:
            login(request, user)
            return ownerhome(request)
        else:
            return HttpResponse("Invalid login details.....")

    return render(request, 'login.html')

def upload1(request):
    form = fileForm
    if request.method == "POST":
        form = fileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home1(request)
    return render(request, 'upload1.html', {'form': form})

def upload(request):
    k=File.objects.all()
    return render(request,'upload.html',{'s':k})
def delete_file(request,pk):
    b=File.objects.get(pk=pk)
    b.delete()
    return upload(request)
def view_file(request,pk):
    b=File.objects.get(pk=pk)
    context = {
        'instance': b,
        'title': 'View File'
    }
    return render(request, 'file.html', context)

def edit_file(request,pk):
    view=File.objects.get(pk=pk)
    form=fileForm(instance=view)
    if request.method == "POST":
        form = fileForm(request.POST,request.FILES,instance=view)
        if form.is_valid():
            form.save(commit=True)
            return home1(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'upload1.html',{'form':form})
def user_logout(request):
    logout(request)
    return home(request)