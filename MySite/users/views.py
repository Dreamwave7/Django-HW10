from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect(to="quotes:index")
    
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:index")
        else:
            render(request,"users/signup.html",context={"form":form})

    return render(request, "users/signup.html", context={"form":RegistrationForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to="quote:index")
    
    if request.method =="POST":
        user = authenticate(username = request.POST["username"], password=request.POST["password"])
        if user is None:
            redirect(to="users:error")

        login(request , user)
        return redirect(to="quotes:index")


    return render(request,"users/login.html", context={"form":LoginForm()})



def error(request):
    return render(request,"users/error.html")

@login_required()
def logoutuser(request):
    logout(request)
    return redirect(to="quotes:index")


















