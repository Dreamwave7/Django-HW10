from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
    return render(request,"quotes/index.html")