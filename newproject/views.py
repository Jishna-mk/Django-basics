from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from newproject.forms import  UserAddForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render (request,"home.html")


def signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is Already Taken")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email is Already taken")
                return redirect("signup")
            else:
                new_user=form.save()
                new_user.save()
                messages.info(request,"New user Created")
                return redirect('signin')

    return render(request, "register.html", {"form": form})


def signin(request):
    if request.method=="POST":
        username=request.POST["uname"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("home")
        else:
            
            messages.info(request,"username or password incorrect")
            return redirect("signin")

    return render(request,"login.html")

def signout(request):

    logout(request)
    return redirect("signin")