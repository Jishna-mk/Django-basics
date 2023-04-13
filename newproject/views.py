from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,"home.html")

def room(request):
    return render(request,"room.html")
def navbar(request):
    return render(request,'navbar.html')
def main(request):
    return render(request,'main.html')

def signup(request):
    if request.method=="POST":
        uname=request.POST.get('Username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("pass word mismatch")
        
        else:
         my_user=User.objects.create_user(uname,email,pass1)
         my_user.save()
         return HttpResponse("new user created")
    
    # return redirect('login')
    return render(request,'registerview.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        
        
    return render(request,'loginview.html')



