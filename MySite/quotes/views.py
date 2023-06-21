from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required
def get_mongo():
    client = MongoClient("mongodb+srv://guest:guest@dreamwave.dhurwpi.mongodb.net/?retryWrites=true&w=majority")
    db = client.module8
    return db


def index(request):
    db = get_mongo()
    quotes = db.quotes.find()
    name = request.user
    return render(request,"quotes/index.html", context={"quotes":quotes,"name":name})

def author_bio(request, author_name):
    print(author_name)
    db = get_mongo()
    author = db.authors.find_one({"fullname":author_name})
    print(author)
    return render(request,"quotes/author.html", context={"author":author})

@login_required
def add_author(request):
    if request.method =="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:index")
        else:
            return render(request, "quotes/add_author.html",{"form":form})

    return render(request,"quotes/add_author.html", context={"form":AuthorForm()})

@login_required
def add_quote(request):
    if request.method =="POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:index")
        else:
            return render(request, "quotes/add_quote.html", context={"form":form})

    return render(request, "quotes/add_quote.html", context={"form":QuoteForm()})















