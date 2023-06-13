from django.shortcuts import render, redirect

from .forms import *

def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to="noteapp:index")
    
    if request.method == "POST":
        

