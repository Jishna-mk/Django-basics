from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"home.html")

def room(request):
    return render(request,"room.html")
def navbar(request):
    return render(request,'navbar.html')
def main(request):
    return render(request,'main.html')
def login(request):
    return render(request,'loginview.html')
def signup(request):
    return render(request,'registerview.html')




